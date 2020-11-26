from django.shortcuts import render, HttpResponse

from .models import *

def homepage(request):
    venues = VenueDetails.objects.all()
    context = {
        "venues" : venues,
    }
    return render(request, 'core/index.html',context)


