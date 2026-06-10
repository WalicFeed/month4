from django.contrib import admin
from . import models

@admin.register(models.HorseTour)
class HorseTourAdmin(admin.ModelAdmin):
    exclude = ('views',)

admin.site.register(models.HorseTourCategory)
admin.site.register(models.Person)
admin.site.register(models.Horse)
admin.site.register(models.Comment)