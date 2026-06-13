from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesListView.as_view(), name='view_categories'),
    path('products/', views.ProductsListView.as_view(), name='view_products'),
    path('categories/<int:category_id>/products/', views.CategoryProductsView.as_view(), name='view_category_products'),
]