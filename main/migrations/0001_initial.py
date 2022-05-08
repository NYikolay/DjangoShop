# Generated by Django 4.0.4 on 2022-05-08 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.PositiveBigIntegerField(default=1, verbose_name='Цена товара')),
                ('quantity_in_stock', models.PositiveSmallIntegerField(default=1, verbose_name='Количество товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_of_products', models.PositiveSmallIntegerField(default=1, verbose_name='Количество покупаемого товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ReturnPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_request', models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.purchase', verbose_name='Покупка')),
            ],
            options={
                'ordering': ['-time_of_request'],
            },
        ),
    ]
