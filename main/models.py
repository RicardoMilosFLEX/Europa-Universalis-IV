from django.db import models
from django import forms
# Create your models here.

class Notes(models.Model):
    title = models.CharField('Название темы', max_length=255)
    notes = models.TextField('Запись')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class User(models.Model):
    login = models.CharField('Имя пользователя', max_length=20)
    email = models.EmailField('Адрес электронной почты')
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.login
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = "Пользователи"