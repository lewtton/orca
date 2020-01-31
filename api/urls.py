from django.urls import path
from . import views, views_pk

urlpatterns = [
    # ex: /polls/
    path('', views.showlist),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:userid>/', views.vote, name='vote'),
    path('info/', views.info),
    path('pk/<int:userid>/', views_pk.apipk, name='apipoker'),
]