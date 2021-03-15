from django.db import models
from django.utils import timezone

from DichVu.models import DichVu
from NguoiDung.models import NguoiDung
from DiaChi.models import province
from DiaChi.models import district
from DiaChi.models import ward
from DiaChi.models import street


class PhongTro(models.Model):
<<<<<<< HEAD
    NguoiDung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE, related_name='PhongTro')
=======
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
    DichVu = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    province = models.ForeignKey(province, on_delete=models.CASCADE)
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    ward = models.ForeignKey(ward, on_delete=models.CASCADE)
    street = models.ForeignKey(street, on_delete=models.CASCADE)
<<<<<<< HEAD
    address = models.CharField(blank=True, max_length=255)  # Địa chỉ
    TieuDe = models.CharField(max_length=100)
    Anh = models.ImageField(upload_to='upload_renting_pic', blank=True)
    Gia = models.DecimalField(max_digits=20, decimal_places=3)
    NgayDang = models.DateField(default=timezone.now)
    NgayCapNhat = models.DateField(auto_now=True, db_index=True)
=======
    TieuDe = models.CharField(max_length=100)
    Anh = models.ImageField(upload_to='', default='images.jpg')
    Gia = models.DecimalField(max_digits=20, decimal_places=3)
    NguoiDung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE, related_name='PhongTro')
    NgayDang = models.DateField(default=timezone.now)
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
    SDT = models.IntegerField(default=0)
    DienTich = models.IntegerField(default=0)
    NoiDung = models.TextField(max_length=1000)

    def __str__(self):
        return self.TieuDe
<<<<<<< HEAD


def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id)


class Images(models.Model):
    phongtro = models.ForeignKey(PhongTro, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload_renting_pic')
=======
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
