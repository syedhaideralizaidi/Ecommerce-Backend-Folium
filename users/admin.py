from django.contrib import admin
from .models import User

class MyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, MyModelAdmin)
