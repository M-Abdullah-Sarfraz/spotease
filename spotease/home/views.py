from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from ads.models import AdPayment  
from .models import Reservation  
from django.contrib.admin.views.decorators import staff_member_required




def home(request):

    ads = AdPayment.objects.all()  
    return render(request, 'homelogin.html', {'ads': ads, 'user': request.user})  

def reserve_spot(request, spot_id):

    ad = get_object_or_404(AdPayment, id=spot_id)

    if request.method == 'POST':

        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        reservation_date = request.POST.get('reservation_date')
        screenshot = request.FILES.get('screenshot') 

        
        if not all([name, start_time, end_time, reservation_date, screenshot]):
            messages.error(request, "All fields are required, including the screenshot.")
            return render(request, 'reserve_spot.html', {'ad': ad})  

        try:

            reservation = Reservation.objects.create(
                ad_payment=ad, 
                name=name,
                start_time=start_time,
                end_time=end_time,
                reservation_date=reservation_date,
                screenshot=screenshot, 
                user=request.user  
            )
            messages.success(request, "Reservation saved successfully!")


            return redirect('home:booking_success')  

        except Exception as e:
            messages.error(request, f"Error occurred while saving reservation: {str(e)}")
            return render(request, 'reserve_spot.html', {'ad': ad})

    return render(request, 'reserve_spot.html', {'ad': ad})

# booking success page
def booking_success(request):
    return render(request, 'booking_success.html')  




def spot_detail(request, spot_id):
    spot = get_object_or_404(AdPayment, id=spot_id)

    if request.method == 'POST':

        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        reservation_date = request.POST.get('reservation_date')


        request.session['reservation_data'] = {
            'name': name,
            'start_time': start_time,
            'end_time': end_time,
            'reservation_date': reservation_date,
            'spot_id': spot_id
        }


        return redirect('home:payment-success', spot_id=spot_id)

    return render(request, 'spot_detail.html', {'spot': spot})

def payment_details(request, spot_id):

    ad = get_object_or_404(AdPayment, id=spot_id)

    if request.method == 'POST':
 
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        reservation_date = request.POST.get('reservation_date')
        screenshot = request.FILES.get('screenshot')  


        if not all([name, start_time, end_time, reservation_date, screenshot]):
            messages.error(request, "All fields are required, including the screenshot.")
            return render(request, 'reserve_spot.html', {'ad': ad}) 

        try:

            reservation = Reservation.objects.create(
                ad_payment=ad,  
                name=name,
                start_time=start_time,
                end_time=end_time,
                reservation_date=reservation_date,
                screenshot=screenshot  
            )
            messages.success(request, "Reservation saved successfully!")


            return redirect('home:payment_success')  

        except Exception as e:
            messages.error(request, f"Error occurred while saving reservation: {str(e)}")
            return render(request, 'reserve_spot.html', {'ad': ad})

    return render(request, 'reserve_spot.html', {'ad': ad})  


def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home:home')  
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
            update_session_auth_hash(request, user)  
            messages.success(request, "Your profile was successfully updated!")
            return redirect('edit_profile')  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# My Ads View 
def my_ads(request):
    if request.user.is_authenticated:  
        ads = AdPayment.objects.filter(user=request.user)  
        return render(request, 'my_ads.html', {'ads': ads})
    else:
        return redirect('login')



def booking_status(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    ad = reservation.ad_payment  

    return render(
        request, 
        'booking_status.html', 
        {'reservation': reservation, 'ad': ad}
    )

def check_booking_status(request):
    try:

        reservation = Reservation.objects.filter(user=request.user).latest('reservation_date')
        return redirect('home:booking_status', reservation_id=reservation.id)
    except Reservation.DoesNotExist:
        messages.error(request, "You don't have any bookings yet.")
        return redirect('home:home') 

# Admin view for accepting or rejecting a booking
@staff_member_required
def update_reservation_status(request, reservation_id, status):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    

    if status not in ['pending', 'confirmed', 'rejected']:
        messages.error(request, "Invalid status!")
        return redirect('admin:app_reservation_change', reservation_id=reservation.id)
    
    reservation.status = status
    reservation.save()

    messages.success(request, f"Reservation status updated to {status.capitalize()}")
    return redirect('home:booking_status', reservation_id=reservation.id)




# Filtered views based on category
def playing_arenas(request):
    ads = AdPayment.objects.filter(category="Playing Arena") 
    return render(request, 'playing_arenas.html', {'ads': ads})

def gyms(request):
    ads = AdPayment.objects.filter(category="Gym")  
    return render(request, 'gyms.html', {'ads': ads})

def farm_house(request):
    ads = AdPayment.objects.filter(category="Farm House")  
    return render(request, 'farmhouse.html', {'ads': ads})

def hotel_room(request):
    ads = AdPayment.objects.filter(category="Hotel Room")  
    return render(request, 'hotelrooms.html', {'ads': ads})

def saloons(request):
    ads = AdPayment.objects.filter(category="Saloon")  
    return render(request, 'saloons.html', {'ads': ads})

def swimming_pools(request):
    ads = AdPayment.objects.filter(category="Swimming Pool")  
    return render(request, 'swimming_pools.html', {'ads': ads})

def cafes(request):
    ads = AdPayment.objects.filter(category="Cafe")  
    return render(request, 'cafes.html', {'ads': ads})

def event_space(request):
    ads = AdPayment.objects.filter(category="Event Space")  
    return render(request, 'event_spaces.html', {'ads': ads})

def houses(request):
    ads = AdPayment.objects.filter(category="House")  
    return render(request, 'houses.html', {'ads': ads})

def shops(request):
    ads = AdPayment.objects.filter(category="Shop")  
    return render(request, 'shops.html', {'ads': ads})

