from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# / Menu
def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names_and_prices = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)
    return HttpResponse(f"Les pizzas: {pizzas_names_and_prices_str}")'''

    pizzas = Pizza.objects.all()


    return render(request, 'menu/index.html', {'pizzas': pizzas})
