from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Anket

admin.site.register(Anket, UserAdmin)
