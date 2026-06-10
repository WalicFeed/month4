from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomLoginForm
from django.core.paginator import Paginator
from django.db.models import F

def register(request):
    if request.method == 'POST':
        form = forms.AnketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login_anket/')
    else:
        form = forms.AnketForm()
    return render(request, 'ankets/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/candidates_anket/')
        context = {'form': form}
    else:
        form = CustomLoginForm(request)
        context = {'form': form}
    return render(request, 'ankets/login.html', context)

def candidates_view(request):
    ankets = models.Anket.objects.all().order_by('-id')
    paginator = Paginator(ankets, 1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ankets/candidates.html', {'candidates': page_obj})

def search_view(request):
    query = request.GET.get('q')
    if query:
        ankets = models.Anket.objects.filter(username__icontains=query).order_by('-id')
    else:
        ankets = models.Anket.objects.all().order_by('-id')
    context = {'query': query, 'candidates': ankets}
    return render(request, 'ankets/candidates.html', context)