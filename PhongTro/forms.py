from django import forms
from .models import PhongTro

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan
from DiaChi.models import province, district, ward, street
from NguoiDung.models import NguoiDung

class PhongTroForm(forms.ModelForm):
    class Meta:
        model = PhongTro
        fields = ('DichVu','TieuDe','province','district','ward','street','Gia','Anh','NguoiDung','NgayDang','SDT','NoiDung','DienTich')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)
        self.fields['district'].queryset = district.objects.none()

        if 'province' in self.data:
            try:
                country_id = int(self.data.get('province'))
                self.fields['district'].queryset = district.objects.filter(_province_id=country_id).order_by('_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province._district_set.order_by('_name')
