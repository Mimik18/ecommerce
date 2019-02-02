from django.test import TestCase
from django.urls import path
from . import views

urlpatterns = [
 
    path('',views.information,name='evenement'),
   # path('register',views.evenementForm,name='register'),
    path('',views.information,name='information')
    
]

