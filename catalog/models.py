from django.db import models
from django.urls import reverse

class Catalog(models.Model):
    name = models.CharField(max_length=128,blank=False,unique=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
       return reverse('home:cataposts', args=[str(self.id)]) 

    class Meta:
        ordering = ['-id']
    @property
    def has_post(self):
        return True if self.post_set.exists() else False
        
