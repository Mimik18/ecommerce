from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class contact(models.Model):
    prenom=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    sujet=models.CharField(max_length=100)
    message=models.CharField(max_length=200)
    envoyeur=models.EmailField(max_length=45)
    id_message=models.AutoField(primary_key=True)
    date_msg=models.DateField(default=timezone.now)
    heure_msg=models.TimeField(default=timezone.now)
    
