from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='course/', null=True, blank=True, verbose_name='превью')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='владелец')
    update = models.DateTimeField(default=None, verbose_name='последнее обновление')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', null=True, blank=True, verbose_name='превью')
    link = models.CharField(max_length=150, null=True, blank=True, verbose_name='ссылка')
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='курс', related_name='lesson')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='владелец')

    def __str__(self):
        return f'{self.title} ({self.course})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('title',)


class Subscription(models.Model):
    users = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='пользователь')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name='курс', related_name='subscription')

    def __str__(self):
        return f'{self.users} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        ordering = ('users',)
