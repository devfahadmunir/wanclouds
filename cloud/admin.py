from django.contrib import admin

# Register your models here.
from .models import item
# here we register table in admin
admin.site.register(item)
