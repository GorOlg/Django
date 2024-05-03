from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('change/', views.change, name='change'),
    path('result/', views.result_no, name='result_no'),
    path('ugad/', views.ugad, name='ugad'),
    path('autobiography/', views.autobiography, name='autobiography'),
]