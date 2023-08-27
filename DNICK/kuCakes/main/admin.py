from django.contrib import admin

from .models import Cake , OrderedCakes

admin.site.register(Cake)
admin.site.register(OrderedCakes)