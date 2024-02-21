from django.shortcuts import render
from django.http import HttpResponse


def qna(req):
    return HttpResponse('product')

def qna_details(req, num):
    return HttpResponse(f'qna_details {num}')

