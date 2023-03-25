from django.contrib import admin
from gallery.models import Astrophotography
# Register your models here.


@admin.register(Astrophotography)
class ObjectAtronomic(admin.ModelAdmin):
    pass
