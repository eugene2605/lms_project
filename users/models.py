from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name='телефон')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='телеграм-ник')
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    METHOD = (
        ('cash', 'наличные'),
        ('non-cash', 'перевод на счет'),
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='пользователь', related_name='payment')
    date_of_payment = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey('materials.Course', on_delete=models.CASCADE, verbose_name='оплаченный курс')
    payment_amount = models.FloatField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=30, choices=METHOD, verbose_name='способ оплаты')
