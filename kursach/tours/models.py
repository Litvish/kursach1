from django.db import models


class Seats(models.Model):
    fio = models.CharField('ФИО', max_length=50)
    email = models.CharField('Почта', max_length=250)
    seat_id = models.TextField('Место')
    date = models.DateTimeField('Дата брони')

    def __str__(self):
        return self.seat_id

    class Meta:
        verbose_name = 'номер места'
        verbose_name_plural = 'номера мест'
