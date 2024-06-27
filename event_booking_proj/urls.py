from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("event_app.urls")),
    path("artists/",include("artist.urls")),
   
]
