from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F

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
        paginator = Paginator(books, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'books': page_obj
        }
        return render(request, template_name = 'books/all_books.html', context = context)
    
def get_book_by_id(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(models.DuneBook, id=book_id)
        views = request.session.get('views', [])
        if book_id not in views:
            book.views = F('views') + 1
            book.save()
            book.refresh_from_db()
        views.append(book_id)
        request.session['views'] = views
        context = {
            'book': book
        }
        return render(request, template_name = 'books/book_by_id.html', context = context)
    
def search_books(request):
    query = request.GET.get('q')
    if query:
        books = models.DuneBook.objects.filter(title__icontains=query).order_by('-id')
    else:
        books = models.DuneBook.objects.all().order_by('-id')
    context = {
        'query': query,
        'books': books
    }
    return render(request, template_name = 'books/all_books.html', context = context)