from django.db import models


# Create your models here.
class TinhTP(models.Model):
    TenTinh = models.CharField(max_length=50)

    def __str__(self):
        return self.TenTinh