from django.db import models
from django.utils import timezone
from ..clients.models import Client
from ..accounts.models import Manager
# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название застройщика или объекта')

    def __str__(self):
        return self.name    

class Apartment(models.Model):
    STATUS_CHOICES = [
        ('Активна', 'Готова к продаже'),
        ('Куплено', 'Куплено'),
        ('Бронь', 'Бронь'),
        ('Рассрочка', 'Рассрочка'),
        ('Отмена', 'Отмена'),
        ('Бартер', 'Бартер'),
    ]

    number = models.CharField(max_length=10, verbose_name='Номер квартиры')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, verbose_name='Застройщик или объект')
    floor = models.PositiveIntegerField(verbose_name='Этаж')
    area = models.FloatField(verbose_name='Квадратура')
    ready_date = models.DateField(verbose_name='Дата готовности к сдаче', default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус', default='Активна')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Клиент')
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Менеджер')
    effect_status = models.TextField(verbose_name='Эффект статуса', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.status == 'Куплено':
            self.effect_status = f'Дата покупки: {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif self.status == 'Бронь':
            self.effect_status = f'Бронь до: {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif self.status == 'Бартер':
            self.effect_status = f'Дата покупки через бартер: {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}'
        elif self.status == 'Рассрочка':
            self.effect_status = f'Рассорчка до: {timezone.now().strftime("%Y-%m-%d %H:%M:%S")}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number}, {self.building.name}'

