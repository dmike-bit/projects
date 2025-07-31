from django.db import models

class MyLibrary(models.Model):
    avtor = models.CharField(max_length=100, verbose_name="Автор")
    composition = models.CharField(max_length=100, verbose_name="Композиция")
    year = models.DateField(verbose_name="Дата произведения")
