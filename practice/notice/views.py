from django.shortcuts import render
from django.http import HttpResponse

def notice(req):
    return HttpResponse('notice')

def notice_free(req):
    return HttpResponse(f'notice_free')

def notice_free_detail(req, num):
    return HttpResponse(f'notice_free_detail {num} 유진선')

def notice_onenone(req):
    return HttpResponse('notice_onenone')

def notice_onenone_detail(req, num):
    return HttpResponse(f'notice_onenone_detail {num} 유진선')

