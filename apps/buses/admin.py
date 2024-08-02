from django.contrib import admin
from .models import Bus, BusCompany

# Register your models here.


admin.site.register(BusCompany)
admin.site.register(Bus)
