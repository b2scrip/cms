#!coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView,ListView
from django.views.generic.edit import UpdateView
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect  
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import PostForm,CommentForm
from .models import Post

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer



class PostCreate(LoginRequiredMixin,FormView):
    login_url = '/user/login/'
    form_class =  PostForm 
    template_name = "post/post_create_form.html"  
    success_url = "/post/list/"

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {
                'message': "Invalid input",
            }
            return JsonResponse(data)
        else:
            return response

    def form_valid(self, form):
        form.instance.author = self.request.user
        #form.save_m2m()
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': "ok",
            }
            return JsonResponse(data)
        else:
            return response
class PostUpdate(UpdateView):
    model = Post
    template_name = "post/post_update.html"
    form_class = PostForm 
    fields = ['title','content','catalog','img']

    def get_object(self, queryset=None):
        obj = Post.objects.get(id=self.kwargs['id'])
        return obj

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all()
    template_name = "post/post_list.html"
    
def postdetail(request,id):
    post_instance = get_object_or_404(Post,pk=id)
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post_instance
                comment.save()
 
                return HttpResponseRedirect(reverse("post:post-detail",args=[post_instance.id]))
    return render(request,
                 'post/post_detail.html',
                 {"post":post_instance,"comment_form":CommentForm()})

@login_required(login_url='/user/login/')
def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid() :
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect(reverse("user:user-profile"))
        messages.add_message(request, messages.INFO, '正文内容不能为空')
    context = {"form":PostForm} 
    return render(request,"post/post_create_form.html",context)

@login_required
def postedit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES,instance=post)
            if form.is_valid() :
                #form.instance.user = request.user
                form.save()
                return HttpResponseRedirect(reverse("user:user-profile"))
        context = {"form":PostForm(initial={"title":post.title,
                                            "content":post.content,
                                            "img":post.img,
                                            "catalog":post.catalog,
                                   })}
        return render(request,"post/post_update_form.html",context)
    else:
        return HttpResponseRedirect(reverse("user:user-profile"))


class PostMixin(object):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostApi(PostMixin, ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

