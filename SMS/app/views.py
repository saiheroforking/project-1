from django.http import HttpResponse
from django.shortcuts import render


rooms = [
    {'id':1,'name':"saikanna"},
    {'id':1,'name':"teja"},
    {'id':1,'name':"prabhu"},
    {'id':1,'name':"kanna"},
]

def home(request):
    context = {'rooms':rooms}
    return render(request,'base.html', context)


def base(request):
    return render(request,'home.html')