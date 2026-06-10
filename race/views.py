from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.db.models import F

def tour_list_view(request):
    if request.method == "GET":
        tours = models.HorseTour.objects.all()
        person_horses = models.Horse.objects.select_related('person').all()
        paginator = Paginator(tours, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "tours": page_obj,
            "person_horses": person_horses,
        }
        return render(request, template_name="race/tours.html", context=context)

def search_view(request):
    query = request.GET.get('q')
    if query:
        tours = models.HorseTour.objects.filter(title__icontains=query).order_by('-id')
    else:
        tours = models.HorseTour.objects.all().order_by('-id')
    person_horses = models.Horse.objects.select_related('person').all()
    context = {
        'tours': tours,
        'person_horses': person_horses,
    }
    return render(request, 'race/tours.html', context)