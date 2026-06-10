from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Anket

@admin.register(Anket)
class AnketAdmin(admin.ModelAdmin):
    exclude = ('views',)