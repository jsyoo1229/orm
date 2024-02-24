from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path('create/<str:title>/', views.product_create, name= 'product_create'),
    path('delete/<int:pk>/', views.product_delete, name= 'product_delete'),
]