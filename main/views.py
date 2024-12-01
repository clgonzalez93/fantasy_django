from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list_view.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def createe(response):
    return render(response, "main/create.html", {})


# python manage.py runserver
