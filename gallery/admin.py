from django.contrib import admin
from gallery.models import AstronomicalObject
# Register your models here.


@admin.register(AstronomicalObject)
class ObjectAtronomic(admin.ModelAdmin):
    pass
