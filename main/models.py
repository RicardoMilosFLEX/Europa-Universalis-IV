from django.db import models

class Notes(models.Model):
    title = models.CharField('Название темы', max_length=255)
    notes = models.TextField('Запись')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
