from django import http
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')
