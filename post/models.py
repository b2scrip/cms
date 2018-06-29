#!coding:utf-8
# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from catalog.models import Catalog
from likedislike.models import LikeDislike
from django.contrib.contenttypes.fields import GenericRelation

from django.urls import reverse
import datetime

#from taggit.managers import TaggableManager


class Post(models.Model):
    title 		= models.CharField(max_length=50,blank=False)
    content 		= RichTextUploadingField(blank=False)
    img 		= models.ImageField(max_length=100,upload_to='fengmian/image/%Y/%m', default='users/image/default_big_14.png', verbose_name='Attach a greaat picture for your post')
    author 		= models.ForeignKey(User,blank=False, on_delete=models.CASCADE)
    votes 		= GenericRelation(LikeDislike, related_query_name='post')
    catalog         	= models.ForeignKey(Catalog, blank=False, on_delete=models.CASCADE,verbose_name="select catalog")
    draft           	= models.BooleanField(default=False)
    publish         	= models.DateField(auto_now=False, auto_now_add=False,default=datetime.date.today)
    read_time       	= models.IntegerField(default=0)
    updated         	= models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp       	= models.DateTimeField(auto_now=False, auto_now_add=True)
#    tags = TaggableManager()
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return  reverse('post:post-detail', kwargs={'id':self.pk})

