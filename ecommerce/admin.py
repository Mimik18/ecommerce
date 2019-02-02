from django.contrib import admin
#from .models import (evenement,encadrant,formation,offre)

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# class NutekAdmin(Adminsite):
#     # site_title=ugettext_lazy('Nutek')

admin_site=MyAdminSite()
admin.site.site_header = 'Fun Shopping '                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'Fun Shopping' #
