from django.shortcuts import render
from . import models


def tour_list_view(request):
    if request.method == "GET":
        tours = models.HorseTour.objects.all()
        person_horses = models.Horse.objects.select_related('person').all()
        context = {
            "tours": tours,
            "person_horses": person_horses,
        }
        return render(request, template_name="race/tours.html", context=context)
