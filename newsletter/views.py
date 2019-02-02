from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from .models import Inscription
from django.contrib import messages
 

def newsletterv(request):
   
    form = Inscription(request.POST)
    
    if form.is_valid(): 

        formscontact=Inscription()
            
           
        formscontact.email = form.cleaned_data['Email']
            
        formscontact.save()
        envoi = True
            # messages.success(request,'Votre message a bien été envoyée')

    return render(request, 'index/index.html',{'form':form})