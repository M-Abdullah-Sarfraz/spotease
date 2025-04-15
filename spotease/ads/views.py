from django.shortcuts import render, redirect
from .forms import AdForm
from .models import Ad

def post_ad(request, category):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.category = category
            ad.save()
            return redirect('choose_category')
    else:
        form = AdForm(initial={'category': category})
    return render(request, f'ads/post_ad/{category.lower().replace(" ", "_")}.html', {'form': form, 'category': category})


def choose_category(request):
    return render(request, 'ads/choose_category.html')


def ads_list(request):
    ads = Ad.objects.all()
    return render(request, 'ads/ads_list.html', {'ads': ads})