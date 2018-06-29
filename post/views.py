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
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import PostForm
from .models import Post

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer


import time
from django.http import StreamingHttpResponse
from django.template.loader import render_to_string

class PostCreate(LoginRequiredMixin,FormView):
    login_url = '/user/join/'
    form_class =  PostForm 
    template_name = "post/post_create_form.html"  
    success_url = "/post/list/"

    def form_invalid(self, form):
        print(form.data)
        print("form invalid...")
        response = super().form_invalid(form)
        print(response)
        if self.request.is_ajax():
            data = {
                'message': "Invalid input",
            }
            return JsonResponse(data)
        else:
            return response

    def form_valid(self, form):
        print("form valid...")
        form.instance.author = self.request.user
        #form.save_m2m()
        response = super().form_valid(form)
        print(response)
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
    return render(request,'post/post_detail.html',{"post":post_instance})

@login_required(login_url='/user/join/')
def postcreate(request):
    if request.method == 'POST':
        print(request.FILES.get("img",None))
        print(request.POST["content"]=="")
        form = PostForm(request.POST,request.FILES)
        if form.is_valid() :
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect("/")
        messages.add_message(request, messages.INFO, '正文内容不能为空')
    context = {"form":PostForm} 
    return render(request,"post/post_create_form.html",context)


class PostMixin(object):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PostApi(PostMixin, ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
def test(request):
    return StreamingHttpResponse(stream_response_generator())


def stream_response_generator():
    
    yield render_to_string('bigpipe.html', {"title":"BigPipe Test Page"})
    for x in range(0,10):
        is_last = False
        if x == 9: is_last = True
        pagelet = dict(id="content_%s" % x, get_html_content=x, 
                        get_css_resources="", get_js_resources="", 
                        is_last=is_last )
        yield render_to_string('pagelet.html',{'pagelet':pagelet})
        
        time.sleep(1)
    yield "</body></html>\n"

