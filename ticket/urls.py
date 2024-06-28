from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # The parent path is path("tickets/", include("ticket.urls"))
    path('', views.getTickets, name='get-tickets'),
    path('create/', views.createTicket, name='create-ticket'),
    path('<str:pk>/', views.getTicket, name='get-ticket'),
    path('<str:pk>/update/', views.updateTicket, name='update-ticket'),
    path('<str:pk>/delete/', views.deleteTicket, name='delete-ticket'),
]
