from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Добавляем пустой путь
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('add_tour/', views.add_tour, name='add_tour'),
]
