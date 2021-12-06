from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def api(request):
    return render(request, 'main/api.html')
