from django.urls import path
from . import views

urlpatterns = [
    path('view_basket/', views.view_basket, name='view_basket'),
    path('create_an_item/', views.create_an_item, name='create_an_item'),
    path('view_basket/<int:item_id>/update/', views.update_an_item, name='update_an_item'),
    path('view_basket/<int:item_id>/delete/', views.delete_an_item, name='delete_an_item'),
]