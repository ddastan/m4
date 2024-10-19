from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import posts


def test_view(request):
    return HttpResponse("Test view")

def main_page_view(request):
    return render(request, 'base.html')

def list_view (request):
    if request.method == 'GET':
        return render(request, 'list.html',)

def details_view(request):
    if request.method == 'GET':
        return render(request, 'details.html')
