# Generated by Django 5.0.1 on 2024-02-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_payment_date_of_payment_alter_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_of_payment',
            field=models.DateField(auto_now_add=True, verbose_name='дата оплаты'),
        ),
    ]
