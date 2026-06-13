from django.urls import path
from . import views

urlpatterns = [
    path('view_basket/', views.BasketListView.as_view(), name='view_basket'),
    path('create_an_item/', views.CreateItemView.as_view(), name='create_an_item'),
    path('view_basket/<int:item_id>/update/', views.UpdateItemView.as_view(), name='update_an_item'),
    path('view_basket/<int:item_id>/delete/', views.DeleteItemView.as_view(), name='delete_an_item'),
]