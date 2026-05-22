from django.shortcuts import render
from django.http import HttpResponse

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
