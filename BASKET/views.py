from django.shortcuts import redirect, render, get_object_or_404
from . import models, forms
from django.views import generic


class BasketListView(generic.ListView):
    template_name = 'crud/basket.html'
    model = models.Basket
    context_object_name = 'items'
    ordering = ['-id']
    paginate_by = 2
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['page_obj']
        return context

class CreateItemView(generic.CreateView):
    template_name = 'crud/create.html'
    model = models.Basket
    form_class = forms.BasketForm
    success_url = '/view_basket/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdateItemView(generic.UpdateView):
    template_name = 'crud/update.html'
    model = models.Basket
    form_class = forms.BasketForm
    pk_url_kwarg = 'item_id'
    success_url = '/view_basket/'
    context_object_name = 'item_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_id'] = context['object']
        return context

class DeleteItemView(generic.DeleteView):
    template_name = 'crud/delete.html'
    model = models.Basket
    pk_url_kwarg = 'item_id'
    success_url = '/view_basket/'


# def view_basket(request):
#     if request.method == 'GET':
#         baskets = models.Basket.objects.all().order_by('-id')
#         context = {
#             'items': baskets
#         }
#         return render(request, 'crud/basket.html', context)
    
# def create_an_item(request):
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('view_basket')
#     else:
#         form = forms.BasketForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'crud/create.html', context)

# def update_an_item(request, item_id):
#     item_id = get_object_or_404(models.Basket, id=item_id)
#     if request.method == 'POST':
#         form = forms.BasketForm(request.POST, request.FILES, instance=item_id)
#         if form.is_valid():
#             form.save()
#             return redirect('view_basket')
#     else:
#         form = forms.BasketForm(instance=item_id)
#     context = {
#         'form': form,
#         'item_id': item_id
#     }
#     return render(request, 'crud/update.html', context)

# def delete_an_item(request, item_id):
#     item = get_object_or_404(models.Basket, id=item_id)
#     item.delete()
#     return redirect('view_basket')