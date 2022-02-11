from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def home_page(request):
    return render(request, 'home.html')
