from django.db import models


class Drive(models.Model):
    name = models.CharField('имя', max_length=50)
    phone = models.CharField('еелефон', max_length=50)
    email = models.CharField('почта', max_length=50)
    auto = models.CharField('машина', max_length=50)
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
