from django.urls import path
from . import views


urlpatterns = [
    path('CineBoard_register/', views.RegisterView.as_view(), name='CineBoard_register'),
    path('CineBoard_login/', views.LoginView.as_view(), name='CineBoard_login'),
    path('CineBoard_logout/', views.LogoutView.as_view(), name='CineBoard_logout'),
    path('CineBoard_create/', views.CreateMovieView.as_view(), name='CineBoard_create'),
    path('CineBoard_view/', views.MovieView.as_view(), name='CineBoard_view'),
    path('CineBoard_view/<int:id>/', views.DetailView.as_view(), name='movie_detail'),
    path('CineBoard_view/<int:id>/update/', views.UpdateMovieView.as_view(), name='movie_update'),
    path('CineBoard_view/<int:id>/delete/', views.DeleteMovieView.as_view(), name='movie_delete'),
]
