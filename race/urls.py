from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.TourListView.as_view(), name='tour_list'),
    path('tours/search/', views.SearchToursView.as_view(), name='race_search'),
]