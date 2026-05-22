from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.my_favourite_book, name='favourite_book'),
]