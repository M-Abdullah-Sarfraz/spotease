from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

CATEGORY_CHOICES = [
    ('Playing Arena', 'Playing Arena'),
    ('Gym', 'Gym'),
    ('Farm House', 'Farm House'),
    ('Saloon', 'Saloon'),
    ('Hotel Room', 'Hotel Room'),
    ('Swimming Pool', 'Swimming Pool'),
    ('Cafe', 'Cafe'),
    ('Event Space', 'Event Space'),
    ('Shop', 'Shop'),
    ('House', 'House'),
]

class AdPayment(models.Model):
    CATEGORY_CHOICES = [
        ('Playing Arena', 'Playing Arena'),
        ('Gym', 'Gym'),
        ('Farm House', 'Farm House'),
        ('Hotel Room', 'Hotel Room'),
        ('Saloon', 'Saloon'),
        ('Swimming Pool', 'Swimming Pool'),
        ('Cafe', 'Cafe'),
        ('Event Space', 'Event Space'),
        ('House', 'House'),
        ('Shop', 'Shop'),
    ]

    BANK_CHOICES = [
    ('meezan', 'Meezan Bank'),
    ('sadapay', 'SadaPay'),
    ('bank_alfalah', 'Bank Alfalah'),
    ('faysal', 'Faysal Bank'),
    ('hbl', 'Habib Bank Limited'),
    ('mcb', 'MCB Bank Limited'),
    ('ubl', 'United Bank Limited'),
    ('nbp', 'National Bank of Pakistan'),
    ('js_bank', 'JS Bank'),
    ('bank_of_punjab', 'Bank of Punjab'),
    ('standard_chartered', 'Standard Chartered Bank'),
    ('albaraka', 'Al Baraka Bank'),
    ('askari', 'Askari Bank'),
    ('bank_islamic', 'Bank Islami Pakistan Limited'),
    # Add more banks as needed
]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        default=1
    )
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='ads/images/')
    account_holder_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    bank = models.CharField(max_length=20, choices=BANK_CHOICES)  # Added choices here
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"

# Spot model
class Spot(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

# Booking model (for user bookings)
class Booking(models.Model):
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)  # Your Spot model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # User who made the booking
    payment_details = models.OneToOneField(AdPayment, on_delete=models.SET_NULL, null=True, blank=True)  # Link to AdPayment

    def __str__(self):
        return f"{self.user.username} - {self.spot.name}"