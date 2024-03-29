from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from firstapp.forms import UserForm


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = f"<h2>Пользователь</h2><h3> Имя - {name}" \
            f"Возраст - {age}</h3>"
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form":userform})



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