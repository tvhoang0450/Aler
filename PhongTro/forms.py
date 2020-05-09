from django import forms
from .models import PhongTro

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan

from NguoiDung.models import NguoiDung

class PhongTroForm(forms.ModelForm):
    class Meta:
        model = PhongTro
        fields = ('DichVu','TinhTP' ,'HuyenQuan','TieuDe','Gia','Anh','DiaChi','NguoiDung','NgayDang','SDT','NoiDung','DienTich')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)
        self.fields['HuyenQuan'].queryset = HuyenQuan.objects.none()

        if 'TinhTP' in self.data:
            try:
                country_id = int(self.data.get('TinhTP'))
                self.fields['HuyenQuan'].queryset = HuyenQuan.objects.filter(TinhTP_id=country_id).order_by('TenHuyen')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['HuyenQuan'].queryset = self.instance.TinhTP.huyenquan_set.order_by('TenHuyen')
