from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.my_favourite_book, name='favourite_book'),
    path('books/', views.get_books, name='get_books'),
    path('books/<int:book_id>/', views.get_book_by_id, name='get_book_by_id'),
]