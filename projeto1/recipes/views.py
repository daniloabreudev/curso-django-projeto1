from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, World i'm a big Developer!")

def sobre(request):
    return HttpResponse("Página Sobre")

def contato(request):
    return HttpResponse("Página Contato")
