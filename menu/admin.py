from django.contrib import admin
from .models import Pizza, Pasta


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']


class PastaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom']


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pasta, PastaAdmin)
