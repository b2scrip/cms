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
from django.urls import path,reverse
from django.contrib.auth.decorators import login_required

from likedislike.views import VotesView
from .models import Video,VideoComment
from .views import (
        VideoCreate,
        VideoList,
        VideoDetail,
)

app_name = "video"

urlpatterns = [
    path(r'list/', VideoList.as_view(),name="video-list"),
    path(r'create/', VideoCreate.as_view(),name="video-create"),
#    path(r'<int:pk>/edit/', postedit,name="post-edit"),
#    path(r'update/(?P<pk>[\w-]+)/', PostUpdate.as_view(),name="post-update"),
    path(r'detail/<int:pk>/', VideoDetail.as_view(),name="video-detail"),
#    path(r'api/create/', PostApi.as_view(),name="postcreate-api"),
    path(r'api/<int:pk>/like/',login_required(VotesView.as_view(model=Video, vote_type=LikeDislike.LIKE)),name='video_like'),
    path(r'api/comment/<int:pk>/like/',login_required(VotesView.as_view(model=VideoComment, vote_type=LikeDislike.LIKE)),name='video_comment_like'),
]
