from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=30)
    venue_size = models.IntegerField()          #used to calculate the number of tickets available
    venue_location = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.venue_name
    
    class Meta:
        ordering = ["-modified_at"]