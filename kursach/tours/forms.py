from .models import Seats
from django.forms import ModelForm, TextInput, DateTimeInput


class SeatsForm(ModelForm):
    class Meta:
        model = Seats
        fields = ['fio', 'email', 'seat_id', 'date']

        widgets = {
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "seat_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'номер места'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }