from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.view_categories, name='view_categories'),
    path('products/', views.view_products, name='view_products'),
    path('categories/<int:category_id>/products/', views.view_category_products, name='view_category_products'),
]