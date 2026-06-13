from django.urls import include, path
from . import views

urlpatterns = [
    path('register_anket/', views.RegisterView.as_view(), name='register'),
    path('login_anket/', views.LoginView.as_view(), name='login'),
    path('candidates_anket/', views.CandidatesListView.as_view(), name='candidates'),
    path('captcha/', include('captcha.urls')),
    path('candidates_anket/search/', views.SearchCandidatesView.as_view(), name='search'),
]