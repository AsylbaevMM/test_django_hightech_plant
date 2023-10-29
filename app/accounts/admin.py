from django.contrib import admin
from .models import MyUser


@admin.register(MyUser)
class PostMyUser(admin.ModelAdmin):
    list_display = ['id', 'is_superuser', 'username', 'is_active']
