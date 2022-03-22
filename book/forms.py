from .models import Booking, Attraction
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import DateInput
class BookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ('user', 'title', 'start_time')
    input_formats=['%d/%m/%Y']
    widgets = {
      'user': forms.TextInput(attrs={'id':'id', 'type':'hidden'}),
      'title': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
      #'start_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%y-%m-%d'),
      'start_time': DateInput(attrs={'type': 'date'}),
 
      }

class AddAttractionForm(forms.ModelForm):
  class Meta:
    model = Attraction
    fields = ('location', 'title', 'image', 'body', 'price')
    widgets = {
      'location': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'id', 'type':'hidden'}),
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'image': forms.FileInput(attrs={'class':'form-control'}),
      'body': forms.Textarea(attrs={'class':'form-control'}),
      'price': forms.NumberInput(attrs={'class':'form-control'}),
    }
