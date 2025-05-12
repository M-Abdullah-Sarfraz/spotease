from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from ads.models import AdPayment  # Assuming AdPayment is the spot model


class Spot(models.Model):
    CATEGORY_CHOICES = [
        ('arena', 'Playing Arena'),
        ('gym', 'Gym'),
        ('farmhouse', 'Farm House'),
        ('saloon', 'Saloon'),
        ('hotel', 'Hotel Room'),
        ('pool', 'Swimming Pool'),
        ('cafe', 'Cafe'),
        ('event', 'Event Space'),
        ('shop', 'Shop'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=200)
    timing = models.CharField(max_length=50)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    









class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]

    ad_payment = models.ForeignKey(AdPayment, on_delete=models.CASCADE)  # Link to the ad
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use custom user model
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    reservation_date = models.DateField()
    screenshot = models.ImageField(upload_to='reservations/screenshots/')  # Save the screenshot
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Status field

    def __str__(self):
        return f"Reservation by {self.name} on {self.reservation_date}"
