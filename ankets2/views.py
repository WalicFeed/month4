from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomLoginForm
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic
from django.http import HttpResponse


class RegisterView(generic.View):
    def get(self, request):
        form = forms.AnketForm()
        return render(request, 'ankets/register.html', {'form': form})
    def post(self, request):
        form = forms.AnketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login_anket/')
        return render(request, 'ankets/register.html', {'form': form})

class LoginView(generic.View):
    def get(self, request):
        form = CustomLoginForm(request)
        return render(request, 'ankets/login.html', {'form': form})
    def post(self, request):
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/candidates_anket/')
        return render(request, 'ankets/login.html', {'form': form})

class CandidatesListView(generic.ListView):
    template_name = 'ankets/candidates.html'
    model = models.Anket
    paginate_by = 1
    ordering = ['-id']
    context_object_name = 'candidates'
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidates'] = context['page_obj']
        return context

class SearchCandidatesView(generic.ListView):
    template_name = 'ankets/candidates.html'
    model = models.Anket
    context_object_name = 'candidates'
    paginate_by = 2
    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return self.model.objects.filter(username__icontains=query).order_by('-id')
        return self.model.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['candidates'] = context['page_obj']
        return context


# def register(request):
#     if request.method == 'POST':
#         form = forms.AnketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/login_anket/')
#     else:
#         form = forms.AnketForm()
#     return render(request, 'ankets/register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(request=request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/candidates_anket/')
#         context = {'form': form}
#     else:
#         form = CustomLoginForm(request)
#         context = {'form': form}
#     return render(request, 'ankets/login.html', context)

# def candidates_view(request):
#     ankets = models.Anket.objects.all().order_by('-id')
#     paginator = Paginator(ankets, 1)  
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'ankets/candidates.html', {'candidates': page_obj})

# def search_view(request):
#     query = request.GET.get('q')
#     if query:
#         ankets = models.Anket.objects.filter(username__icontains=query).order_by('-id')
#     else:
#         ankets = models.Anket.objects.all().order_by('-id')
#     context = {'query': query, 'candidates': ankets}
#     return render(request, 'ankets/candidates.html', context)