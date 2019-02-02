from django.shortcuts import render
from .models import commande,produit
import random
# from .forms import commandeForm
# Create your views here.
def commande2(request):
    responses=["index/images/img_bg_2.jpg","index/images/classes-2.jpg","index/images/classes-3.jpg","index/images/classes-4.jpg","index/images/classes-5.jpg","index/images/classes-6.jpg"]
    # list=[]
    res=produit.objects.filter(vendu=False).order_by('id_produit')[:9]
    
    # for x in range (6):
    #     bot_message = random.choice(responses) 
    #      list.append(bot_message)

    return render(request,'formation/formation2.html',locals(),{'res',res})
