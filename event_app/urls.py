from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # The parent path is path("", include("event_app.urls"))
    path('', views.getEvents, name='get-events'),
    path('events/create/', views.createEvent, name='create-event'),
    path('events/<str:pk>/', views.getEvent, name='get-event'),
    path('events/<str:pk>/update/', views.updateEvent, name='update-event'),
    path('events/<str:pk>/delete/', views.deleteEvent, name='delete-event'),
]
