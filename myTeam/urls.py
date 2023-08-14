from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name = 'team'),
    path('player/<int:id>', views.player, name = 'player'),
    path('login', views.login, name='login')
]