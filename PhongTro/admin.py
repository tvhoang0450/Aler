from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import PhongTro, Images


class ImageInline(admin.TabularInline):
    model = Images
    extra = 5


class PhongTroAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

    def save_model(self, request, obj, form, change):
        super(PhongTroAdmin, self).save_model(request, obj, form, change)
        # obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.images.create(file=afile)


admin.site.register(PhongTro, PhongTroAdmin)
=======
from .models import PhongTro

admin.site.register(PhongTro)
>>>>>>> 2c68a77a700e53c38815547a749e531e88085729
