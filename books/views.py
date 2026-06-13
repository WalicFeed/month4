from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic
from datetime import datetime


class MyFavouriteBookView(generic.TemplateView):
    template_name = 'my_favourite_book.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "Dune",
            'author': "Frank Herbert",
            'publication_year': 1965,
            'genre': "Science Fiction",
            'advice': "Read it if you can"
        })
        return context

class BooksListView(generic.ListView):
    template_name = 'books/all_books.html'
    model = models.DuneBook
    paginate_by = 1
    ordering = ['-id']
    context_object_name = 'books'
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['page_obj']
        return context

class BookDetailView(generic.DetailView):
    template_name = 'books/book_by_id.html'
    model = models.DuneBook
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request
        views = request.session.get('views', [])
        book_id = obj.pk
        if book_id not in views:
            self.model.objects.filter(pk=book_id).update(views=F('views')+1)
            views.append(book_id)
            request.session['views'] = views
            obj.refresh_from_db()
        return obj

class SearchBooksView(generic.ListView):
    template_name = 'books/all_books.html'
    model = models.DuneBook
    context_object_name = 'books'
    paginate_by = 2
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return self.model.objects.filter(title__icontains=query).order_by('-id')
        return self.model.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['books'] = context['page_obj']
        return context


# def my_favourite_book(request):
#     if request.method == 'GET':
#         context = {
#             'title': "Dune",
#             'author': "Frank Herbert",
#             'publication_year': 1965,
#             'genre': "Science Fiction",
#             'advice': "Read it if you can"
#         }
#         return render(request, 'my_favourite_book.html', context)

# def get_books(request):
#     if request.method == 'GET':
#         books = models.DuneBook.objects.all().order_by('-id')
#         paginator = Paginator(books, 1)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context = {
#             'books': page_obj
#         }
#         return render(request, template_name = 'books/all_books.html', context = context)
    
# def get_book_by_id(request, book_id):
#     if request.method == 'GET':
#         book = get_object_or_404(models.DuneBook, id=book_id)
#         views = request.session.get('views', [])
#         if book_id not in views:
#             book.views = F('views') + 1
#             book.save()
#             book.refresh_from_db()
#         views.append(book_id)
#         request.session['views'] = views
#         context = {
#             'book': book
#         }
#         return render(request, template_name = 'books/book_by_id.html', context = context)
    
# def search_books(request):
#     query = request.GET.get('q')
#     if query:
#         books = models.DuneBook.objects.filter(title__icontains=query).order_by('-id')
#     else:
#         books = models.DuneBook.objects.all().order_by('-id')
#     context = {
#         'query': query,
#         'books': books
#     }
#     return render(request, template_name = 'books/all_books.html', context = context)