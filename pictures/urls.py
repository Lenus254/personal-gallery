from django.urls import path
from . import views

app_name = 'pictures'

urlpatterns = [
   path('', views.index, name='index'),
   # path('search/', views.search_results, name='search'),
]