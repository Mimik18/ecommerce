from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class utilisateur(models.Model):
    id_utilisateur=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=45)
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    
    
   


class produit(models.Model):#id_produit','categorie','nom','desc_produit','cout','vendu'
    categorie=models.CharField(max_length=100)
    cout=models.IntegerField()
    desc_produit=models.TextField(null=False)
    id_produit=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    vendu=models.BooleanField()
   

    def __str__ (self):
        return self.nom
class commande(models.Model):
    
    id_commande=models.AutoField(primary_key=True)
    produi=models.ForeignKey(produit, on_delete=models.CASCADE)
    user=models.ForeignKey(utilisateur, on_delete=models.CASCADE)
    TYPE_PAIEMENT_CHOICES=(
        ('cb','carte_bancaire'),
        ('espece','espece'),
        ('en_ligne','en_ligne')
    )
    type_paiement=models.CharField(max_length=30,
    choices=TYPE_PAIEMENT_CHOICES,
    default='espece')
    #l'utilisateur doit avoir un attribut qui indique la commande a laquelle il a été inscrit
    etat_paiement=models.BooleanField(default=False)
    date_paiement=models.DateTimeField(default=timezone.now)

   

    def __str__ (self):
        return self.id_commande



