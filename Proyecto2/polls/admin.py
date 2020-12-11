from django.contrib import admin

from .models import Question ,Choice,Clientes,Articulos,Pedidos

admin.site.register(Question)

admin.site.register(Choice)

admin.site.register(Clientes)

admin.site.register(Articulos)

admin.site.register(Pedidos)