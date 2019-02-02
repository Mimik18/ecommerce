"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('index/', include('error.urls')),
     path('acceuil/', include('index.urls')),
    path('',include('index.urls')),
    path('produits/', include('commandes.urls')),
    path('commande',include('commandes.urls')),
    # path('evenement/', include('evenement.urls')),
    # path('register',include('evenement.urls')),
    # path('offre/', include('offre.urls')),
    # path('description/', include('offre.urls')),
    # path('formation/', include('formation.urls')),
    # path('inscription/', include('inscription.urls')),
    path('contact/', include('contact.urls')),
    # path('payment/', include('payment.urls')),
    # path('information/', include('evenement.urls')),
    #    path('contactForm/', include('contact.urls')),
    path(
    'admin/password_reset/',
    auth_views.PasswordResetView.as_view(),
    name='admin_password_reset',),
path(
    'admin/password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done',),
path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm',),
path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete',),
]
handler404 = 'error.views.error_404_view'
#handler500 = 'my_app.views.handler500'
#admin.site.site_header = 'Nutek'                    # default: "Django Administration"
admin.site.index_title = 'Administration du site'                 # default: "Site administration"
admin.site.site_title = 'Nutek' # default: "Django site admin"

