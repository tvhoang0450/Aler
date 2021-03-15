from django.db import models

# Create your models here.

class DichVu(models.Model):
    TenDV = models.CharField(max_length=50)

    def __str__(self):
        return self.TenDV