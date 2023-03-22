from django.contrib import admin
from gallery.models import ObjectAstronomic
# Register your models here.


@admin.register(ObjectAstronomic)
class ObjectAtronomic(admin.ModelAdmin):
    pass
