from django.db import models

class Basket(models.Model):
    user = models.CharField(max_length=255, verbose_name='Пользователь')
    product = models.CharField(max_length=255, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user} - {self.product} ({self.quantity})'