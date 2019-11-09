from django.contrib import admin
from . import models
from .models import Flower, Family, Gardener


# TODO: Implement movie, person and country model admins

class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'family')
    list_filter = ('name', 'family', "gardener__last_name")
    pass


admin.site.register(Flower, FlowerAdmin)

admin.site.register(Family)
admin.site.register(Gardener)
