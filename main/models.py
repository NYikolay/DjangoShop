from django.db import models
from users.models import User


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField('Описание товара')
    price = models.PositiveBigIntegerField('Цена товара', default=1)
    quantity_in_stock = models.PositiveSmallIntegerField('Количество товара', default=1)
    created_at = models.DateTimeField(auto_now_add='True', verbose_name='Дата добавления товара')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity_of_products = models.PositiveSmallIntegerField(default=1, verbose_name='Количество покупаемого товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['-created_at']

    def __str__(self):
        return f'Купил {self.user}, товар {self.product}, количество {self.quantity_of_products}'


class ReturnPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, verbose_name='Покупка')
    time_of_request = models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')

    class Meta:
        verbose_name = 'Возврат покупки'
        verbose_name_plural = 'Возврат покупок'
        ordering = ['-time_of_request']

    def __str__(self):
        return f'Возврат от пользователя {self.purchase.user}, ' \
               f'товар {self.purchase.product}, ' \
               f'количество {self.purchase.quantity_of_products}'
