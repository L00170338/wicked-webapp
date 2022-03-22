from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Attraction(models.Model):
    FLIGHT_FROM = [
        ('Warszawa', 'Warszawa'),
        ('Katowice', 'Katowice'),
        ('Wrocław', 'Wrocław'),
        ('Gdańsk', 'Gdańsk'),
        ('Kraków', 'Kraków'),
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    min_height = models.CharField(max_length=100, default='1.2M')
    max_weight = models.CharField(max_length=100, default='120KG')
    def __str__(self):
        return self.title + ' | ' + str(self.location)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=12, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)  
    street = models.CharField(max_length=50, null=True, blank=True)
    housenumber = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.title + ' | ' + str(self.user)

    @property
    def get_html_title(self):
        return self.title + ' | ' + str(self.user)
