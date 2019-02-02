from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template 

# Create your views here.
# def index(request):
#      return HttpResponse("You're looking at question ")

def index(request):
    #template = get_template("index\event.html")
    #return HttpResponse(template.render)
    return render(request,'index/vet.html')

