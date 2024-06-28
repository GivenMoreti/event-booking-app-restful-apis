from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # The parent path is path("venues/", include("venue.urls"))
    path('', views.getVenues, name='get-venues'),
    path('create/', views.createVenue, name='create-venue'),
    path('<str:pk>/', views.getVenue, name='get-venue'),
    path('<str:pk>/update/', views.updateVenue, name='update-venue'),
    path('<str:pk>/delete/', views.deleteVenue, name='delete-venue'),
]
