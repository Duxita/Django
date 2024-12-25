from django.shortcuts import render
from .forms import UserRegister


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})

def sign_up_by_html(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})