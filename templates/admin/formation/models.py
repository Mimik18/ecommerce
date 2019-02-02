from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class formation(models.Model):
    categorie=models.CharField(max_length=100)
    certifie=models.BooleanField()
    cout=models.IntegerField()
    description=models.TextField(null=False)
    debut_formation=models.DateTimeField()
    fin_formation=models.DateTimeField()
    id_formation=models.IntegerField(unique=True)
    lieu=models.CharField(max_length=30)
    methode_de_formation=models.CharField(max_length=30)
    place_limite=models.IntegerField()
    place_reserve=models.IntegerField()
    #type de formation:formation continu,..
    type_formation=models.CharField(max_length=100)
    nom_formation=models.CharField(max_length=100,default='')

    def __str__ (self):
        return self.nom_formation

