from django.shortcuts import redirect, render, get_object_or_404
from . import models, forms
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'CineBoard/register.html', {'form': form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CineBoard_login')
        return render(request, 'CineBoard/register.html', {'form': form})

class LoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'CineBoard/login.html', {'form': form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('CineBoard_view')
        return render(request, 'CineBoard/login.html', {'form': form})

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('CineBoard_login')

class MovieView(generic.ListView):
    template_name = 'CineBoard/view.html'
    model = models.Movie
    context_object_name = 'movies'
    paginate_by = 2
    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        query = self.request.GET.get('q', '')
        genre = self.request.GET.get('genre', '')
        if query:
            queryset = queryset.filter(title__icontains=query)
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['selected_genre'] = self.request.GET.get('genre', '')
        context['genres'] = self.model.objects.values_list('genre', flat=True).distinct()
        context['movies'] = context['page_obj']
        return context

class DetailView(generic.DetailView):
    template_name = 'CineBoard/movie_detail.html'
    model = models.Movie
    context_object_name = 'movie'
    pk_url_kwarg = 'id'

class CreateMovieView(generic.CreateView):
    template_name = 'CineBoard/create.html'
    model = models.Movie
    form_class = forms.MovieForm
    success_url = '/CineBoard_view/'

class UpdateMovieView(generic.UpdateView):
    template_name = 'CineBoard/update.html'
    model = models.Movie
    form_class = forms.MovieForm
    pk_url_kwarg = 'id'
    success_url = '/CineBoard_view/'

class DeleteMovieView(generic.DeleteView):
    template_name = 'CineBoard/delete.html'
    model = models.Movie
    pk_url_kwarg = 'id'
    success_url = '/CineBoard_view/'
