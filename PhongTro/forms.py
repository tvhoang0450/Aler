from django import forms
<<<<<<< HEAD
from django.forms.widgets import Input

from .models import PhongTro, Images
=======
from .models import PhongTro
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729

from DichVu.models import DichVu
from TinhTP.models import TinhTP

from HuyenQuan.models import HuyenQuan
from DiaChi.models import province, district, ward, street
from NguoiDung.models import NguoiDung

<<<<<<< HEAD

class PhongTroForm(forms.ModelForm):
    NoiDung = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control texteditor-content', 'placeholder': 'Nhập bình luận của bạn tại đây !!!'}))
    TieuDe = forms.CharField(label="", widget=Input(
        attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Nhập tiêu đề của bạn tại đây !!!'}))
    # province = forms.ModelChoiceField(label="c", queryset=province.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control sm-width w-100', 'placeholder': 'Chọn tỉnh !!!'}))
    # district = forms.ModelChoiceField(label="c", queryset=district.objects.none(),
    #                                   widget=forms.Select(attrs={'class': 'form-control sm-width w-100', 'placeholder': 'Chọn tỉnh !!!'}))
    # ward = forms.ModelChoiceField(label="c", queryset=ward.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control sm-width w-100', 'placeholder': 'Chọn tỉnh !!!'}))
    # street = forms.ModelChoiceField(label="c", queryset=street.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control sm-width w-100', 'placeholder': 'Chọn tỉnh !!!'}))

    class Meta:
        model = PhongTro
        fields = (
            'DichVu', 'TieuDe', 'province', 'district', 'ward', 'street', 'Gia', 'SDT',
            'NoiDung', 'DienTich', 'Anh')
=======
class PhongTroForm(forms.ModelForm):
    class Meta:
        model = PhongTro
        fields = ('DichVu','TieuDe','province','district','ward','street','Gia','Anh','NguoiDung','NgayDang','SDT','NoiDung','DienTich')

>>>>>>> 2c68a77a700e53c38815547a749e531e88085729

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.data)
        self.fields['district'].queryset = district.objects.none()

        if 'province' in self.data:
            try:
<<<<<<< HEAD
                province_id = int(self.data.get('province'))
                self.fields['district'].queryset = district.objects.filter(_province_id=province_id).order_by('_name')
=======
                country_id = int(self.data.get('province'))
                self.fields['district'].queryset = district.objects.filter(_province_id=country_id).order_by('_name')
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province._district_set.order_by('_name')
<<<<<<< HEAD


class ImageForm(forms.ModelForm):
    # image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image',)
=======
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
