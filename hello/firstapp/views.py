from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    return render(request, "firstapp/home.html")

def about(request):
    return HttpResponse('<h1> About site</h1>')

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid=1):
    category = request.GET.get("cat", "")
    output = f'<h1> Product number: {productid} Категория {category}</h1>'
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Вано")
    output = f'<h1> Username: {name} Userid: {id}'
    return HttpResponse(output)