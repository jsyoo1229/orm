from django.contrib import admin
from django.urls import path
from .views import qna, qna_details

urlpatterns = [    
    path('', qna),
    path('<int:num>/', qna_details),
]
   