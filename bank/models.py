from django.db import models

class Check(models.Model):
    title = models.CharField(max_length=100,verbose_name="Название банка")
    author = models.CharField(max_length=50, verbose_name="Имя пользователя")
    cchet = models.IntegerField(verbose_name="Номер счета")
    money = models.IntegerField(verbose_name="Деньги на балансе")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True,verbose_name="Описание")

    def __str__(self):
        return self.title