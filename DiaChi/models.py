from django.db import models


# Create your models here.

class province(models.Model):
    _name = models.CharField(max_length=50)
    _code = models.CharField(max_length=20)

    def __str__(self):
        return self._name


class district(models.Model):
    _name = models.CharField(max_length=100)
    _prefix = models.CharField(max_length=20)
    _province = models.ForeignKey(province, on_delete=models.CASCADE)

    def __str__(self):
        return self._name


class street(models.Model):
    _name = models.CharField(max_length=100)
    _prefix = models.CharField(max_length=20)
    _province = models.ForeignKey(province, on_delete=models.CASCADE)
    _district = models.ForeignKey(district, on_delete=models.CASCADE)

    def __str__(self):
        return self._name


class ward(models.Model):
    _name = models.CharField(max_length=100)
    _prefix = models.CharField(max_length=20)
    _province = models.ForeignKey(province, on_delete=models.CASCADE)
    _district = models.ForeignKey(district, on_delete=models.CASCADE)

    def __str__(self):
        return self._name