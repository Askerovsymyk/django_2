

from django.contrib import admin
from user.models import Profiles
# Register your models here.


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_filter = ("user",)