from django.urls import path
from . import views

urlpatterns = [
    path('register_anket/', views.register, name='register'),
    path('login_anket/', views.login_view, name='login'),
    path('candidates_anket/', views.candidates_view, name='candidates'),
]