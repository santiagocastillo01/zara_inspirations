from django.urls import path, include
from zar.views import*
from . import views


urlpatterns = [
    path('',home, name="home"),
    path('inspiraciones/',views.inspiraciones, name='inspiraciones'),
    path('contacto',views.contacto, name='contacto'),
    path('perfumes/',views.perfumes, name='perfumes')
]
