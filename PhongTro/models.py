from django.db import models
from django.utils import timezone

from DichVu.models import DichVu
from NguoiDung.models import NguoiDung
from DiaChi.models import province
from DiaChi.models import district
from DiaChi.models import ward
from DiaChi.models import street


class PhongTro(models.Model):
    DichVu = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    province = models.ForeignKey(province, on_delete=models.CASCADE)
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    ward = models.ForeignKey(ward, on_delete=models.CASCADE)
    street = models.ForeignKey(street, on_delete=models.CASCADE)
    TieuDe = models.CharField(max_length=100)
    Anh = models.ImageField(upload_to='', default='images.jpg')
    Gia = models.DecimalField(max_digits=20, decimal_places=3)
    NguoiDung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE, related_name='PhongTro')
    NgayDang = models.DateField(default=timezone.now)
    SDT = models.IntegerField(default=0)
    DienTich = models.IntegerField(default=0)
    NoiDung = models.TextField(max_length=1000)

    def __str__(self):
        return self.TieuDe
