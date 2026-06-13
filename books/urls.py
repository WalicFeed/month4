from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.MyFavouriteBookView.as_view(), name='favourite_book'),
    path('books/', views.BooksListView.as_view(), name='get_books'),
    path('books/<int:book_id>/', views.BookDetailView.as_view(), name='get_book_by_id'),
    path('search/', views.SearchBooksView.as_view(), name='search_books'),
]