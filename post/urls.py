"""prodct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from likedislike.models import LikeDislike
from .models import Post
from django.urls import path
from django.contrib.auth.decorators import login_required
from likedislike.views import VotesView
from .views import (
        PostCreate,
        PostList,
        PostUpdate,
        PostApi,
        postdetail,
        postcreate,test
)

app_name = "post"

urlpatterns = [
#   path(r'list/', PostList.as_view(),name="post-list"),
    path(r'test/', test,name="test"),
    path(r'create/', postcreate,name="post-create"),
    path(r'update/(?P<pk>[\w-]+)/', PostUpdate.as_view(),name="post-update"),
    path(r'detail/<int:id>/', postdetail,name="post-detail"),
    path(r'api/create/', PostApi.as_view(),name="postcreate-api"),
    path(r'api/<int:pk>/like/',login_required(VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),name='post_like'),
]
