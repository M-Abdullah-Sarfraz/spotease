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

class Ad(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        default=1  # Assuming user with ID=1 exists as a default user
    )
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='ads/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"
