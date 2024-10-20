from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from .models import Post


def test_view(request):
    return HttpResponse("Test view")

def main_page_view(request):
    return render(request, 'base.html')

def list_view (request):
    posts = Post.objects.all()
    if request.method == 'GET':
        return render(request, 'posts/list.html',{'posts':posts})

def details_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'posts/details.html')
