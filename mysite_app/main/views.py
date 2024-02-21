from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse('index')

def about(req):
    return HttpResponse('about')

def contact(req):
    return HttpResponse('contact')


