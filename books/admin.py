from django.contrib import admin
from . import models

@admin.register(models.DuneBook)
class DuneBookAdmin(admin.ModelAdmin):
    exclude = ('views',)