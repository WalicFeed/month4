from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

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
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/candidates_anket/')
        context = {'form': form}
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
    return render(request, 'ankets/login.html', context)

def candidates_view(request):
    ankets = models.Anket.objects.all().order_by('-id')
    return render(request, 'ankets/candidates.html', {'candidates': ankets})