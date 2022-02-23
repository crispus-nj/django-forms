from django.contrib import admin

from pizza.models import Pizza, Size

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Size)