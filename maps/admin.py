from django.contrib import admin
from .models import Locais


class LocaisAdmin(admin.ModelAdmin):
    pass


admin.site.register(Locais, LocaisAdmin)
