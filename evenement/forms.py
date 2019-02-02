from django import forms

class EvenementForm(forms.Form):
    # cout=forms.CharField(max_length=5)
    # duree=forms.IntegerField()
    # nombre_place_limite=forms.IntegerField()
    # nombre_place_reserve=forms.IntegerField()
    # type_evenement=forms.CharField(max_length=100)
    # date_evenement=forms.DateField()
    nom_evenement=forms.CharField(max_length=100)
    nom=forms.CharField(max_length=100)
    Prenom=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=40)
    TYPE_PAIEMENT_CHOICES=(
        ('cb','carte_bancaire'),
        ('espece','espece'),
        ('en_ligne','en_ligne')
    )
    type_paiement=forms.CharField(max_length=30)
