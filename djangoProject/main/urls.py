from django.urls import path
from .views import home,about,contacts

urlpatterns = [
    path('',home),
    path('home',home),
    path('about',about),
    path('contacts',contacts)
]