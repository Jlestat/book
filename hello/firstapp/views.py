from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from django')

def about(request):
    return HttpResponse('<h1> About site</h1>')

def contact(request):
    return HttpResponse('<h2>Contacts</h2>')

def products(request, productid=1):
    output = f'<h1> Product number: {productid}</h1>'
    return HttpResponse(output)

def users(request, id=1, name='Вано'):
    output = f'<h1> Username: {name} Userid: {id}'
    return HttpResponse(output)