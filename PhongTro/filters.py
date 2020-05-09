from django import forms

import django_filters
from .models import PhongTro
from HuyenQuan.models import HuyenQuan
from TinhTP.models import TinhTP


def huyenquans(request):
    if request is None:
        return HuyenQuan.objects.none()

    TinhTP = request.user.TinhTP
    return TinhTP.huyenquan_set.all()


class PhongTroFilter(django_filters.FilterSet):
    Gia = django_filters.NumberFilter()
    Gia__gt = django_filters.NumberFilter(field_name='Gia', lookup_expr='gt')
    Gia__lt = django_filters.NumberFilter(field_name='Gia   ', lookup_expr='lt')
    DienTich = django_filters.NumberFilter(lookup_expr='lte')

    class Meta:
        model = PhongTro
        fields = ('DichVu', 'TinhTP', 'HuyenQuan', 'Gia', 'DienTich')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     print(self.data)
    #     self.fields['HuyenQuan'].queryset = HuyenQuan.objects.none()
    #
    #     if 'TinhTP' in self.data:
    #         try:
    #             country_id = int(self.data.get('TinhTP'))
    #             self.fields['HuyenQuan'].queryset = HuyenQuan.objects.filter(TinhTP_id=country_id).order_by('TenHuyen')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['HuyenQuan'].queryset = self.instance.TinhTP.huyenquan_set.order_by('TenHuyen')
