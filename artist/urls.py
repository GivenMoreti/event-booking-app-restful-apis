from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #parent path is path("artists/",include("artists.urls"))
    path('',views.getArtists),
    path("create/",views.createArtist),
    path("<str:pk>/",views.getArtist),
    path("<str:pk>/update",views.updateArtist),
    path("<str:pk>/delete",views.deleteArtist),

]