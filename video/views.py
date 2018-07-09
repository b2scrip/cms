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

from .forms import VideoCreateForm,CommentForm
from .models import Video

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
#from .permissions import IsOwnerOrReadOnly
#from .serializers import PostSerializer



class VideoCreate(LoginRequiredMixin,FormView):
    login_url = '/user/login/'
    form_class =  VideoCreateForm 
    template_name = "video/video_create_form.html"  
    #success_url = "/video/list/"
    success_url = "/"

    def form_invalid(self, form):
        return  super().form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return   super().form_valid(form)
#class PostUpdate(UpdateView):
#    model = Post
#    template_name = "post/post_update.html"
#    form_class = PostForm 
#    fields = ['title','content','catalog','img']
#    def get_object(self, queryset=None):
#        obj = Post.objects.get(id=self.kwargs['id'])
#        return obj

class VideoList(ListView):
    model = Video
    context_object_name = 'videos'
    queryset = Video.objects.all()
    paginate_by = 20
    template_name = "Video/video_list.html"

class VideoDetail(DetailView):
    model = Video
    template_name = 'video/video_detail.html'
    context_object_name = "video"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['recommend_videos'] = Video.objects.order_by('?')[:10]
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.video =  self.get_object()
                comment.save()
                return HttpResponseRedirect(reverse("video:video-detail",args=[self.get_object().id]))
