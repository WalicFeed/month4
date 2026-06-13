from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic


class CategoriesListView(generic.ListView):
    template_name = 'categories.html'
    model = models.Category
    context_object_name = 'categories'
    def get_queryset(self):
        return self.model.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductsListView(generic.ListView):
    template_name = 'products.html'
    model = models.Product
    context_object_name = 'products'
    def get_queryset(self):
        return self.model.objects.select_related('category').all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryProductsView(generic.ListView):
    template_name = 'category_products.html'
    model = models.Product
    context_object_name = 'products'
    pk_url_kwarg = 'category_id'
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return self.model.objects.filter(category_id=category_id)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = get_object_or_404(models.Category, id=category_id)
        return context


# def view_categories(request):
#     categories = models.Category.objects.all()
#     context = {
#         'categories': categories
#     }
#     return render(request, 'categories.html', context)

# def view_products(request):
#     products = models.Product.objects.select_related('category').all()
#     context = {
#         'products': products
#     }
#     return render(request, 'products.html', context)

# def view_category_products(request, category_id):
#     category = models.Category.objects.get(id=category_id)
#     products = models.Product.objects.filter(category=category)
#     context = {
#         'category': category,
#         'products': products
#     }
#     return render(request, 'category_products.html', context)