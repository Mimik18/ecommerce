from django.contrib import admin
from .models import commande,utilisateur,produit
# Register your models here.
#admin.site.register(commande)
@admin.register(commande)
class commandeAdmin(admin.ModelAdmin):
    list_display=('id_commande','type_paiement','etat_paiement','date_paiement')
    list_editable=['etat_paiement']
    list_filter=['etat_paiement']
@admin.register(produit)
class produitAdmin(admin.ModelAdmin):
    list_display=('id_produit','categorie','nom','desc_produit','cout','vendu')
    list_editable=['desc_produit']
    list_filter=['desc_produit']
    ordering=['id_produit']
    search_fields=['categorie','nom']
    save_as=True
    save_on_top=True
@admin.register(utilisateur)
class utilisateurAdmin(admin.ModelAdmin):
    list_display=('id_utilisateur','prenom','nom','email')
    list_editable=['email']
    list_filter=['nom']

    

   
    