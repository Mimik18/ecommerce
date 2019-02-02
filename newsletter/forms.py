from django.apps import AppConfig
from django import forms



    
# Create your models here.
class Inscription(forms.Form):
    email = forms.EmailField(max_length=254,required='true')
    # is_active = forms.BooleanField(_('is active'),)

    # class Meta:
    #     abstract = True
    #     verbose_name = _('subscription')
    #     verbose_name_plural = _('subscriptions')

    def __str__(self):
        return self.email
