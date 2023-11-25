from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from .models import Notes, User
admin.site.register(Notes)
admin.site.register(User)
