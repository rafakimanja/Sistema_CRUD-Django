from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import home, salvar, editar, update, apagar

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', apagar, name='deletar')
]
