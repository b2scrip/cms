from django.db import models
from django.contrib.auth.models import User
from likedislike.models import LikeDislike
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse

from catalog.models import Catalog
import datetime

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100,verbose_name="video name")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    iframe = models.CharField(max_length=500)
    votes  = GenericRelation(LikeDislike, related_query_name='video')
    catalog             = models.ForeignKey(Catalog, blank=False, on_delete=models.CASCADE,verbose_name="select catalog")
    img                 = models.ImageField(max_length=100,upload_to='video/image/%Y/%m', default='video/image/muli.jpg', verbose_name='A picture for your video')
    draft               = models.BooleanField(default=False)
    publish             = models.DateField(auto_now=False, auto_now_add=False,default=datetime.date.today)
    watch_time           = models.IntegerField(default=0)
    updated             = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp           = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse('video:video-detail', kwargs={'pk':self.pk})

class VideoComment(models.Model):
    content = models.TextField()
    video = models.ForeignKey(Video,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes  = GenericRelation(LikeDislike, related_query_name='comment_video')
    parent = models.ForeignKey('self',blank=True, null=True,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_time']
        verbose_name = 'comment_video'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s's Comment" % self.author.username

