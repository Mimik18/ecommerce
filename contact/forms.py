from django import forms

class contactForm(forms.Form):
    Prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    envoyeur = forms.EmailField(label="Votre adresse e-mail",widget=forms.TextInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    Sujet = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    # def __init__(self, request, *args, **kwargs):
    #     super(contactForm, self).__init__(*args, **kwargs)
        # self.fields['team_choice'].queryset = Team.objects.all().filter(team_hr_admin = request.User)