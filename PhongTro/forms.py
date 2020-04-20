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



