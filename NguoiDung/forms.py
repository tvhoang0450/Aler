from django import forms
from .models import NguoiDung
from django.contrib.auth.forms import UserCreationForm

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan

from NguoiDung.models import NguoiDung

class NguoiDungForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NguoiDung
        fields = ('username','email','DiaChi', 'GioiTinh', 'NgaySinh')



