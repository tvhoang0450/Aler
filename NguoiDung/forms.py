from django import forms
from .models import NguoiDung
from django.contrib.auth.forms import UserCreationForm

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan

from NguoiDung.models import NguoiDung

<<<<<<< HEAD

class NguoiDungForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NguoiDung
        fields = ('username', 'email', 'DiaChi', 'GioiTinh', 'NgaySinh')
=======
class NguoiDungForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NguoiDung
        fields = ('username','email','DiaChi', 'GioiTinh', 'NgaySinh')



>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
