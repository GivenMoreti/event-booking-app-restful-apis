from django.db import models
from artist.models import Artist

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=50)
    event_location = models.CharField(max_length=100)
    event_artists = models.ManyToManyField(Artist,verbose_name="artists for the event")
    event_start_date = models.DateTimeField(null=True)
    event_created = models.DateTimeField(auto_now_add=True)
    event_modified = models.DateTimeField(auto_now=True)

    def __Str__(self):
        return f"The title of the event is {self.event_title}"
    
    class Meta:
        ordering = ["event_created"]