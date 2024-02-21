from django.contrib import admin
from django.urls import path
from .views import product_list, product_details

urlpatterns = [    
    path('', product_list),
    path('<int:num>/', product_details),
]
   