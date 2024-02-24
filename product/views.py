from django.shortcuts import render, redirect
from .models import Post
from django.db.models import Q

def product_list(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        Posts = Post.objects.filter(Q(title__icontains = q) | Q(content__icontains = q)).distinct()
    else:
        Posts = Post.objects.all()
    context = {"db": Posts}
    return render(request, "product/product_list.html", context)


def product_detail(request, pk):
    Post_One = Post.objects.get(pk = pk)
    context = {"db": Post_One}
    return render(request, "product/product_detail.html", context)

def product_create(request, title):
    contents = f"hello world {title}"
    q = Post.objects.create(title = title, contents = contents)
    q.save()
    return redirect('product_list')

def product_delete(request, pk):
    q = Post.objects.delete(pk = pk)
    return redirect('product_list')