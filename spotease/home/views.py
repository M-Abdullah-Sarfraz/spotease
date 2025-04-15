from django.shortcuts import render
from .models import Spot

def home_view(request):
    spots_by_category = {}
    categories = ['arena', 'gym', 'farmhouse', 'saloon', 'hotel', 'pool', 'cafe', 'event', 'shop']

    for category in categories:
        spots_by_category[category] = Spot.objects.filter(category=category)[:5]  # Fetch top 5 spots per category

    return render(request, 'home.html', {'spots_by_category': spots_by_category})
