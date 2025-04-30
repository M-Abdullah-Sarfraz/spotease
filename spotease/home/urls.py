from django.urls import path
from . import views

app_name = 'home'  # Define the namespace for the 'home' app

urlpatterns = [
    path('', views.home, name='home'),
    path('spot/<int:spot_id>/', views.spot_detail, name='spot_detail'),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_ads/', views.my_ads, name='my_ads'),
    path('playing-arenas/', views.playing_arenas, name='playing-arenas'), 
    path('gyms/', views.gyms, name='gyms'), 
    path('farm-house/', views.farm_house, name='farm-house'), 
    path('hotel-rooms/', views.hotel_room, name='hotel-rooms'), 
    path('saloons/', views.saloons, name='saloons'), 
    path('swimming-pools/', views.swimming_pools, name='swimming-pools'), 
    path('cafes/', views.cafes, name='cafes'), 
    path('event-spaces/', views.event_space, name='event-spaces'),  
    path('houses/', views.houses, name='houses'), 
    path('shops/', views.shops, name='shops'), 
]
