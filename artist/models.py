from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=30,null=True)
    artist = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    # courses = models.ManyToManyField(Course,through='Enrollment')
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_modified = models.DateTimeField(auto_now=True,blank=True,null=True)


    def __str__(self):
         return self.artist_name