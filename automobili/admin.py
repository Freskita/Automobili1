from django.contrib import admin

from .models import Marca, Cliente, Auto, Concessionario, Acquisto


admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Concessionario)
admin.site.register(Acquisto)