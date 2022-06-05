from dataclasses import fields
import django_filters
from .models import doctor


class doctorfilter(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='icontains')
    Specialization=django_filters.CharFilter(lookup_expr='icontains')
    address=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = doctor
        fields = '__all__'
        exclude = ['image','create_at','phone']