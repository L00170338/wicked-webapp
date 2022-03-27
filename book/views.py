from book.models import Profile, Attraction, Booking
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .filters import Filters
#
from .forms import BookingForm, AddAttractionForm
from datetime import datetime
from datetime import timedelta
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Booking
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #get attractions from logged attraction agency 
        location = self.kwargs['pk']
        attractions_in_location = Attraction.objects.filter(location=self.kwargs['pk'])
        attractions = []
        for attraction in attractions_in_location:
            attractions.append(attraction)
        #get today date
        date = datetime.today()
        calendar = Calendar(date.year, date.month, attractions)
        #call the formatmonth method, which returns our calendar as a table
        html_calendar = calendar.formatmonth(withyear=True)
        #own html templates is trusted, about 'html_calendar'
        context['calendar'] = mark_safe(html_calendar)
        return context

class Book(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'book.html'
    success_url = reverse_lazy('home')

    def get_initial(self, *args, **kwargs):
        initial = {}
        title = Attraction.objects.get(id=self.kwargs['pk'])
        initial['title'] = title.title
        return initial

class BookEdit(generic.UpdateView):
    model = Booking
    template_name = 'booking_edit.html'
    form_class = BookingForm
    success_url = reverse_lazy('home')

class YourBooking(generic.ListView):
    model = Booking
    template_name = 'your_booking.html'

    def get_context_data(self, *args, **kwargs):
        context = {}
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        book = Booking.objects.filter(user=page_user.user)
        context["book"] = book
        return context

class BookDelete(generic.DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('home')

class Home(generic.ListView):
    model = Attraction
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Filters(self.request.GET, queryset=self.get_queryset())
        return context

class CurrentTrip(generic.DetailView):
    model = Attraction
    template_name = 'currenttrip.html'

class AddAttraction(generic.CreateView):
    #check this view
    model = Attraction
    form_class = AddAttractionForm
    template_name = 'addattraction.html'
    success_url = reverse_lazy('home')
