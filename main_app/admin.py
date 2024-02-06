from django.contrib import admin
# import your models here
from .models import Boat, Cleaning, Captain

# Register your models here
admin.site.register(Boat)
admin.site.register(Cleaning)
admin.site.register(Captain)


