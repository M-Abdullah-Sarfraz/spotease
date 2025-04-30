# home/views.py

from django.shortcuts import render, get_object_or_404, redirect
from ads.models import Ad  
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from ads.models import Ad


def home(request):
    ads = Ad.objects.all()  # Query all ads from the ads database
    return render(request, 'homelogin.html', {'ads': ads, 'user': request.user})  # Pass the logged-in user to the template

def spot_detail(request, spot_id):
    # Fetch the specific spot from the Ad model by its ID
    spot = get_object_or_404(Ad, id=spot_id)
    return render(request, 'spot_detail.html', {'spot': spot})

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # or you can redirect to a thank-you page
        else:
            messages.error(request, "Please fix the errors in the form.")
    else:
        form = ContactForm()

    return render(request, 'contactus.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # This keeps the user logged in after changing password
            messages.success(request, "Your profile was successfully updated!")
            return redirect('edit_profile')  # Redirect to the edit profile page after successful update
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# My Ads View
def my_ads(request):
    if request.user.is_authenticated:  # Ensure the user is logged in
        ads = Ad.objects.filter(user=request.user)  # Filter ads posted by the logged-in user
        return render(request, 'my_ads.html', {'ads': ads})
    else:
        # Redirect to login if user is not authenticated
        return redirect('login')
    



def playing_arenas(request):
    ads = Ad.objects.filter(category="Playing Arena")  # Filter ads by category
    return render(request, 'playing_arenas.html', {'ads': ads})
def gyms(request):
    ads = Ad.objects.filter(category="Gym")  # Filter ads by category
    return render(request, 'gyms.html', {'ads': ads})
def farm_house(request):
    ads = Ad.objects.filter(category="Farm House")  # Filter ads by category
    return render(request, 'farmhouse.html', {'ads': ads})
def hotel_room(request):
    ads = Ad.objects.filter(category="Hotel Room")  # Filter ads by category
    return render(request, 'hotelrooms.html', {'ads': ads})
def saloons(request):
    ads = Ad.objects.filter(category="Saloon")  # Filter ads by category
    return render(request, 'saloons.html', {'ads': ads})
def swimming_pools(request):
    ads = Ad.objects.filter(category="Swimming Pool")  # Filter ads by category
    return render(request, 'swimming_pools.html', {'ads': ads})
def cafes(request):
    ads = Ad.objects.filter(category="Cafe")  # Filter ads by category
    return render(request, 'cafes.html', {'ads': ads})
def event_space(request):
    ads = Ad.objects.filter(category="Event Space")  # Filter ads by category
    return render(request, 'event_spaces.html', {'ads': ads})
def houses(request):
    ads = Ad.objects.filter(category="House")  # Filter ads by category
    return render(request, 'houses.html', {'ads': ads})
def shops(request):
    ads = Ad.objects.filter(category="Shop")  # Filter ads by category
    return render(request, 'shops.html', {'ads': ads})
