from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


def index(request):
    data = {'age': 50}
    return render(request, "firstapp/index.html", context=data)

def about(request):
    return render(request, "firstapp/about.html")

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