from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.db.models import Sum
 
 
class LikeDislikeManager(models.Manager):
    use_for_related_fields = True
 
    def likes(self):
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
 
    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )
 
    vote = models.SmallIntegerField(verbose_name="vote", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="user",on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 
    objects = LikeDislikeManager()
    def posts(self):
        return self.get_queryset().filter(content_type__model='post')
