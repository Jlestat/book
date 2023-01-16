from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from django')

def about(request):
    return HttpResponse('<h1> About site</h1>')

def contact(request):
    return HttpResponse('<h2>Contacts</h2>')