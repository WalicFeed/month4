from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def my_favourite_book(request):
    if request.method == 'GET':
        context = {
            'title': "Dune",
            'author': "Frank Herbert",
            'publication_year': 1965,
            'genre': "Science Fiction",
            'advice': "Read it if you can"
        }
        return render(request, 'my_favourite_book.html', context)

def get_books(request):
    if request.method == 'GET':
        books = models.DuneBook.objects.all().order_by('-id')
        context = {
            'books': books
        }
        return render(request, template_name = 'books/all_books.html', context = context)
    
def get_book_by_id(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(models.DuneBook, id=book_id)
        context = {
            'book': book
        }
        return render(request, template_name = 'books/book_by_id.html', context = context)