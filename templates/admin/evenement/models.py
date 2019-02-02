from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class evenement(models.Model):
    cout=models.CharField(max_length=100)
    duree=models.IntegerField()
    id_evenement=models.IntegerField(unique=True)
    nombre_place_limite=models.IntegerField()
    nombre_place_reserve=models.IntegerField()
    type_evenement=models.CharField(max_length=100)
    date_evenement=models.DateField()
    nom_evenement=models.CharField(max_length=100,default='')
