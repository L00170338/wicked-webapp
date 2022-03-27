from book.models import Attraction, Location
from django.contrib import admin
from .models import Profile, Location, Attraction, Booking
# Register your models here.
admin.site.register(Location)
admin.site.register(Attraction)
admin.site.register(Profile)
admin.site.register(Booking)