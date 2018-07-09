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

    def check_who_like_this_post(self):
        if self.votes.likes().exists():
            return [like.user  for like in self.votes.likes()]
        else:
            return None
    
    def get_absolute_url(self):
        return  reverse('post:post-detail', kwargs={'id':self.pk})
    def get_instance_catalog(self):
        return self.catalog.name

    @classmethod
    def get_posts_for_homepage(cls):
        return cls.objects.all()[:5]
    @classmethod
    def get_posts_catalog(cls):
        return cls.objects.first().get_instance_catalog()

    @property
    def get_comments_count(self):
        return self.comment_set.count()


class Comment(models.Model):
    content = models.TextField()

#    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#    object_id = models.PositiveIntegerField()
#    content_object = GenericForeignKey()

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes  = GenericRelation(LikeDislike, related_query_name='comment')
    parent = models.ForeignKey('self',blank=True, null=True,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_time']
        verbose_name = 'comment'
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s's Comment" % self.author.username
