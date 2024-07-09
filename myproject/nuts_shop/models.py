from django.db import models
from django.core.validators import MinValueValidator
from django.forms import forms


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя клиента')
    password = models.CharField(max_length=48, widget=forms.PasswordInput())
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    date_registered = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
