from django import forms

import django_filters
from .models import PhongTro


class PhongTroFilter(django_filters.FilterSet):
    Gia = django_filters.NumberFilter(lookup_expr='lte')
    DienTich = django_filters.NumberFilter(lookup_expr='lte')
    class Meta:
        model = PhongTro
        fields = ('DichVu', 'TinhTP', 'HuyenQuan', 'Gia', 'DienTich')
