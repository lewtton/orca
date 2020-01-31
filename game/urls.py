from django.urls import path
from . import views, views_pk

urlpatterns = [
    # ex: /polls/
    path('', views.index),
    path('poker/<int:userid>/', views.table),
    path('poker/', views.yard),
    path('poker/<int:userid>/apipk/', views_pk.apipk, name='apipoker'),
]