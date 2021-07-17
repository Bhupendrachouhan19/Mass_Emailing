from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name ='home'),
    path('send', views.loginuser, name ='send'),
]
