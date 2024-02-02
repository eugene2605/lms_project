# Generated by Django 5.0.1 on 2024-02-01 18:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_alter_lesson_course'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_payment', models.DateField(verbose_name='дата оплаты')),
                ('payment_amount', models.FloatField(verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'наличные'), ('non-cash', 'перевод на счет')], max_length=30, verbose_name='способ оплаты')),
                ('paid_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='оплаченный курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]