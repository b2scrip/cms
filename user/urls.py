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
from django.urls import path
from django.conf import settings
from .views import (
        JoinFormView,
        SignUpView,
        user_posts_detail,
        user_posts_gallery,
        signup,
        profile_setting,
        user_profile,
        user_like_posts,
)

from django.contrib.auth.views import logout,login
app_name = "user"

urlpatterns = [
    path(r'join/', signup,name="usersignup"),
    path(r'login/', login,{'template_name': 'user/login.html'},name="userlogin"),
    path(r'logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path(r'<int:id>/posts/', user_posts_detail,name="user-posts"),
    path(r'<int:id>/gallery/', user_posts_gallery,name="user-posts-gallery"),
    path(r'setting/', profile_setting,name="profile-setting"),
    path(r'profile/', user_profile,name="user-profile"),
    path(r'<int:id>/user-like-posts/', user_like_posts,name="user-like-posts"),
   
]
