from dataclasses import fields
import django_filters
from .models import Post


class blogfilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    description=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['image','create_at','subject','create_by','slug']