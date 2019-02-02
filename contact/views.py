from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from .forms import contactForm
from .models import contact
from django.contrib import messages
 

# def contact(request):
    
#     return render(request,'contact/contact.html')
def contactv(request):
   
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    # form = ContactForm(request.POST or None)
    form = contactForm(request.POST)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    try:
        if form.is_valid(): 
            formscontact=contact()
            # # Ici nous pouvons traiter les données du formulaire
            # formscontact.prenom = 'Prenom'
            formscontact.prenom = form.cleaned_data['Prenom']
            formscontact. nom = form.cleaned_data['nom']
            formscontact.envoyeur = form.cleaned_data['envoyeur']
            formscontact.message = form.cleaned_data['message']
            formscontact.sujet = form.cleaned_data['Sujet']
            # formscontact.sujet ='hkhlhkjjb'
            # # Nous pourrions ici envoyer l'e-mail grâce aux données 
            # # que nous venons de récupérer
            # formscontact=contact.objects.create(Prenom='nisrine',nom='khan',envoyeur='sdfjlq@gmail.com',message='jlfdsqm',sujet='kjslfkqj')
            formscontact.save()
            envoi = True
            messages.success(request,'Votre message a bien été envoyée')

    except Exception as e:
        messages.warning(request,"Une erreur  {} s'est produite lors de l'envoi de votre message".format(e))

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'contact/contact.html',{'form':form})