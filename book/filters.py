from dataclasses import fields
import django_filters
from .models import book


class bookfilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = book
        fields = '__all__'
        exclude = ['image','create_at','book']