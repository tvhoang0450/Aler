from django.db import models

# Create your models here.
from TinhTP.models import TinhTP


class HuyenQuan(models.Model):
    TenHuyen = models.CharField(max_length=100)
    TinhTP = models.ForeignKey(TinhTP, on_delete=models.CASCADE)

    def __str__(self):
        return self.TenHuyen