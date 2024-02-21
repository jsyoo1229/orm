from django.contrib import admin
from django.urls import path
from .views import notice, notice_free, notice_free_detail, notice_onenone, notice_onenone_detail

urlpatterns = [    
    path('', notice),
    path('free/', notice_free),
    path('free/<int:num>', notice_free_detail),
    path('onenone/', notice_onenone),
    path('onenone/<int:num>', notice_onenone_detail),
]
   