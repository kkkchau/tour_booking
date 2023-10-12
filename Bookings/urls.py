from django.urls import path

from . import views


app_name='Bookings'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registration', views.registration, name='registration'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('bookTour', views.bookTour, name='bookTour'),
    path('bookingResult', views.bookingResult, name='bookingResult'),
    path('bookingConfirmation', views.bookingConfirmation, name='bookingConfirmation'),
    path('catalog', views.catalog, name='catalog'),
    path('myBooking', views.myBooking, name='myBooking'),
]