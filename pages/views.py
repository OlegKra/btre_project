from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    ctx = {
        "listings": listings,
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
    }
    return render(request, 'pages/index.html', ctx)


def about(request):
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    ctx = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors,        
    }
    return render(request, 'pages/about.html', ctx)