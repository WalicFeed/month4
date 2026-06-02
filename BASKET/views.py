from django.shortcuts import redirect, render, get_object_or_404
from . import models, forms

def view_basket(request):
    if request.method == 'GET':
        baskets = models.Basket.objects.all().order_by('-id')
        context = {
            'items': baskets
        }
        return render(request, 'crud/basket.html', context)
    
def create_an_item(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_basket')
    else:
        form = forms.BasketForm()
    context = {
        'form': form
    }
    return render(request, 'crud/create.html', context)

def update_an_item(request, item_id):
    item_id = get_object_or_404(models.Basket, id=item_id)
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES, instance=item_id)
        if form.is_valid():
            form.save()
            return redirect('view_basket')
    else:
        form = forms.BasketForm(instance=item_id)
    context = {
        'form': form,
        'item_id': item_id
    }
    return render(request, 'crud/update.html', context)

def delete_an_item(request, item_id):
    item = get_object_or_404(models.Basket, id=item_id)
    item.delete()
    return redirect('view_basket')