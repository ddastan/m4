from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def test_view(request):
    return HttpResponse("Test view")

def main_page_view(request):
    return render(request, 'base.html')
