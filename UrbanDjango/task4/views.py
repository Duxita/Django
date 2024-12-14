from django.shortcuts import render

def platform(request):
    context = {
        'title': 'Игровая платформа',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'content': ''

    }
    return render(request, 'fourth_task/platform.html', context)

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
        'content': games

    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    context = {
        'title': 'Корзина',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'content': 'Ваша корзина сейчас пуста'
    }
    return render(request, 'fourth_task/cart.html', context)
