from django.contrib import admin
from .models import Inscription
# Register your models here.
@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display=('email','is_active')