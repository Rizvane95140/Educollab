from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_discussion(request):
    message = "Salut !"
    return HttpResponse(message)
