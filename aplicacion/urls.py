from django.urls import path, include
from .views import index, saludo, pablo
urlpatterns = [
    #urls de aplicacion:
    path('', index,name='index'),
    path('saludo/', saludo, name='saludo'),
    path('pablo/', pablo, name='pablo'),
]