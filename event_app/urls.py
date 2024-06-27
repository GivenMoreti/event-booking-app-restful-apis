from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.getEvents),
    path("/events/create/",views.createEvent),
    path("/events/<str:pk>/",views.getEvent),
    path("/events/<str:pk>/update/",views.updateEvent),
    path("/events/<str:pk>/delete",views.deleteEvent)
]
