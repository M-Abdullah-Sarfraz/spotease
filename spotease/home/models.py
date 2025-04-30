from django.db import models

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