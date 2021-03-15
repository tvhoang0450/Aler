from django.contrib import admin

# Register your models here.
from .models import province, district, ward, street

admin.site.register(province)
admin.site.register(district)
admin.site.register(ward)
admin.site.register(street)