from math import floor

from django.shortcuts import render
from pkg_resources import resource_stream

from .forms import ResourceForm


def resource_calculator(request):
    result = None  # Inicializa o resultado como `None`
    resources = None
    troops = None
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            wood = form.cleaned_data['wood']
            food = form.cleaned_data['food']
            gold = form.cleaned_data['gold']
            stone = form.cleaned_data['stone']

            # Realize os cálculos aqui
            resources = {
                'total_wood': wood * 20,
                'total_food': food * 20,
                'total_gold': gold * 20,
                'total_stone': stone * 20
            }

            def milita_calculator(food: int, gold: int):
                if food/60 < 1 or gold/20 < 1:
                    return "You can't produce militia."
                return floor(min(food/60, gold/20))

            def archer_calculator(wood: int, gold: int):
                if wood/25 < 1 or gold/45 < 1:
                    return "You can't produce archers."
                return floor(min(wood/25, gold/45))

            def scout_calculator(food: int):
                if food/80 < 1:
                    return "You can't produce scouts."
                return floor(food/80)

            troops = {
                'militia': milita_calculator(resources['total_food'], resources['total_gold']),
                'archer': archer_calculator(resources['total_wood'], resources['total_gold']),
                'scout': scout_calculator(resources['total_food'])
            }
    else:
        form = ResourceForm()

    context = {
        'form': form,
        'resources': resources,
        'troops': troops
    }

    return render(request, 'build_creator_app/resource_form.html', context)
