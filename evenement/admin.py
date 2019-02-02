from django.contrib import admin
from .models import evenement

# Register your models here.
@admin.register(evenement)
class evenementAdmin(admin.ModelAdmin):
    list_display=('id_evenement','nom_evenement','date_evenement','type_evenement','nombre_place_reserve','nombre_place_limite','duree')
    list_editable=('date_evenement','type_evenement','duree')
    list_filter=['date_evenement']

