from django.shortcuts import render
from . import models

def view_categories(request):
    categories = models.Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)

def view_products(request):
    products = models.Product.objects.select_related('category').all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def view_category_products(request, category_id):
    category = models.Category.objects.get(id=category_id)
    products = models.Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_products.html', context)