# Generated by Django 5.2 on 2025-04-12 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Назва виробника')),
            ],
            options={
                'verbose_name': 'Виробник',
                'verbose_name_plural': 'Виробники',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва послуги')),
                ('description', models.TextField(blank=True, verbose_name='Опис послуги')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна послуги, грн')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Зображення послуги')),
            ],
            options={
                'verbose_name': 'Послуга',
                'verbose_name_plural': 'Послуги',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва товару')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна, грн')),
                ('btu', models.CharField(choices=[('07', '07 BTU'), ('09', '09 BTU'), ('12', '12 BTU'), ('18', '18 BTU'), ('24', '24 BTU'), ('28', '28 BTU'), ('36', '36 BTU')], max_length=3, verbose_name='Потужність (BTU)')),
                ('area_coverage', models.CharField(choices=[('20', 'До 20 м² (07 BTU)'), ('25', 'До 25 м² (09 BTU)'), ('35', 'До 35 м² (12 BTU)'), ('50', 'До 50 м² (18 BTU)'), ('60', 'До 60 м² (24 BTU)'), ('80', 'До 80 м² (28 BTU)'), ('100', 'До 100 м² (36 BTU)')], max_length=3, verbose_name='Площа покриття (м²)')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Основне зображення')),
                ('is_available', models.BooleanField(default=True, verbose_name='В наявності')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='airinua.manufacturer', verbose_name='Виробник')),
            ],
            options={
                'verbose_name': 'Кондиціонер',
                'verbose_name_plural': 'Кондиціонери',
                'ordering': ['manufacturer', 'name'],
            },
        ),
        migrations.CreateModel(
            name='FeedbackRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я клієнта")),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('contact_method', models.CharField(choices=[('telegram', 'Telegram'), ('viber', 'Viber'), ('call', 'Дзвінок')], max_length=10, verbose_name="Спосіб зв'язку")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='airinua.product', verbose_name='Товар (якщо є)')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_at'],
            },
        ),
    ]
