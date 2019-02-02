from django.contrib import admin
from .models import contact
# Register your models here.
#admin.site.register(formation)
@admin.register(contact)
class formationAdmin(admin.ModelAdmin):
    list_display=('id_message','prenom','nom','sujet','envoyeur')
    # list_editable=['debut_formation']
    # list_filter=['debut_formation']
