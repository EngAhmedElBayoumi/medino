from dataclasses import fields
import django_filters
from .models import illnesses


class illfilter(django_filters.FilterSet):
    illness_name=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = illnesses
        fields = '__all__'
        exclude = ['image','create_at','create_by','slug','diagnosis','Symptoms','protection','about_illness']