from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='wmarkt_home'),
    path('about/', views.about, name='about_Wochenmarkt'),
    path('register/', views.register, name='register'),
]