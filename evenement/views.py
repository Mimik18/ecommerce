from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from .forms import EvenementForm
from .models import evenement

# Create your views here.
def information(request):
    res=evenement.objects.all().order_by('date_evenement')[:9]
    # for x in range (6):
    #     bot_message = random.choice(responses) 
    #      list.append(bot_message)

    return render(request,'evenement/information.html',locals(),{'res',res})
