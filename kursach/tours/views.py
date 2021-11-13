from django.shortcuts import render, redirect
from .models import Seats
from .forms import SeatsForm
from django.views.generic import DetailView


def tours_home(request):
    tours = Seats.objects.order_by('date')
    return render(request, 'tours/tours_home.html', {'tours': tours})


class ToursDetailView(DetailView):
    model = Seats
    template_name = 'tours/details_view.html'
    context_object_name = 'seat'


def create(request):
    error = ''
    if request.method == 'POST':
        form = SeatsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверна'

    form = SeatsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'tours/create.html', data)
