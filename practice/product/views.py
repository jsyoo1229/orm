from django.shortcuts import render
from django.http import HttpResponse

product_list = [
    {
        "id": 1,
        "title": "장고는 너무 재미있어!!!",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "파이썬도 너무 재미있어!!!!",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "자바스크립트는 별로였어!!!",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]


def product_list(req):
    context = {'product_list': product_list}
    return (req, 'product_list.html', context)

def product_details(req, num):
    return HttpResponse(f'product_details {num} 유진선')

