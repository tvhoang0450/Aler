import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone


class NguoiDung(AbstractUser):
    DiaChi = models.CharField(max_length=100, default='')
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    GioiTinh = models.IntegerField(choices=GENDER_CHOICES, default=GENDER_MALE)
    NgaySinh = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.username
