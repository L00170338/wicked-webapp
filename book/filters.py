import django_filters
from .models import Attraction

class Filters(django_filters.FilterSet):
    class Meta:
        model = Attraction
        fields = {
            'title': ['icontains'],
        }