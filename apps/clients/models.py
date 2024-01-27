from django.db import models

# Create your models here.


class Client(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО клиента')
    client_number = models.CharField(max_length=15, unique=True, verbose_name='Номер клиента')
    contract_number = models.CharField(max_length=20, unique=True, verbose_name='Номер договора')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
