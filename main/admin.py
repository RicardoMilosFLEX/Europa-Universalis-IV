from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Notes
admin.site.register(Notes)

