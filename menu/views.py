from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Pasta


# / Menu
def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names_and_prices = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)
    return HttpResponse(f"Les pizzas: {pizzas_names_and_prices_str}")"""

    pizzas = Pizza.objects.all().order_by('prix')
    pasta = Pasta.objects.all().order_by('prix')

    return render(request, 'menu/index.html', {'pizzas': pizzas,
                                               'pasta': pasta,
                                               })


def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)


def api_get_pastas(request):
    pastas = Pasta.objects.all().order_by('prix')
    json = serializers.serialize("json", pastas)
    return HttpResponse(json)