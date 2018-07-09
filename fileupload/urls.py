# encoding: utf-8
from django.urls import path
from django.contrib.auth.decorators import login_required
from fileupload.views import (
        BasicVersionCreateView, BasicPlusVersionCreateView,
        jQueryVersionCreateView, AngularVersionCreateView,
        PictureCreateView, PictureDeleteView, PictureListView,
        )

app_name = "upload"

urlpatterns = [
#    path('basic/', BasicVersionCreateView.as_view(), name='upload-basic'),
#    path('basic/plus/', BasicPlusVersionCreateView.as_view(), name='upload-basic-plus'),
#    path('new/', PictureCreateView.as_view(), name='upload-new'),
    path('angular/', login_required(AngularVersionCreateView.as_view()), name='upload-angular'),
#    path('jquery-ui/', jQueryVersionCreateView.as_view(), name='upload-jquery'),
    path('delete/<int:pk>', login_required(PictureDeleteView.as_view()), name='upload-delete'),
    path('view/', login_required(PictureListView.as_view()), name='upload-view'),
]
