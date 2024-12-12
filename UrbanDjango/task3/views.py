from django.shortcuts import render
from django.shortcuts import render

def platform(request):
    context = {
        'title': 'Игровая платформа',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'craft': '/craft/'}
    }
    return render(request, 'templates/third_task/platform.html', context)

def games(request):
    games = {
        "Game1": "FarCry",
        "Game2": "Fallout",
        "Game3": "Half-Life"
    }
    context = {
        'title': 'Игры',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'games': games}
    return render(request, 'templates/third_task/games.html', context)

def cart(request):
    context = {
        'title': 'Корзина',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'message': 'Ваша корзина сейчас пуста.'
    }
    return render(request, 'templates/third_task/cart.html', context)
