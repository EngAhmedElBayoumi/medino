from dataclasses import fields
import django_filters
from .models import advice


class advicefilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = advice
        fields = '__all__'
        exclude = ['image','create_at','description']