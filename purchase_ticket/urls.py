from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # The parent path is path("", include("purchase_ticket.urls"))
    path('', views.getPurchases, name='get-purchases'),
    path('create/', views.createPurchase, name='create-purchase'),
    path('<str:pk>/', views.getPurchase, name='get-purchase'),
    path('<str:pk>/update/', views.updatePurchase, name='update-purchase'),
    path('<str:pk>/delete/', views.deletePurchase, name='delete-purchase'),
]
