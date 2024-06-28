from django.db import models
from artist.models import Artist
from venue.models import Venue

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=50)
    event_location = models.CharField(max_length=100)
    event_venue = models.ForeignKey(Venue,on_delete=models.CASCADE,null=True)
    event_artists = models.ManyToManyField(Artist,verbose_name="artists for the event")
    event_start_date = models.DateTimeField(null=True)
    event_created = models.DateTimeField(auto_now_add=True)
    event_modified = models.DateTimeField(auto_now=True)

    def __Str__(self):
        return f"{self.event_title} at {self.event_location} {self.event_venue}"
    
    class Meta:
        ordering = ["-event_created"]