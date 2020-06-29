from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name, age):
    return HttpResponse('<h1>Hello {} age {}</h1>'.format(name, age))
