from datetime import timedelta, datetime, timezone

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Subscription, Course
from users.models import User


@shared_task
def send_mail_to_subscribers(title, course_id):
    subscriptions = Subscription.objects.filter(course_id=course_id)
    course = Course.objects.get(pk=course_id)
    if subscriptions:
        delta = timedelta(minutes=1)
        now = datetime.now(timezone.utc)
        if now - course.update > delta:
            for sub in subscriptions:
                send_mail(
                    f'Обновление по курсу {title}',
                    f'Внимание! Вышло обновление по курсу {title}. Срочно смотри, чтобы быть в курсе!',
                    settings.EMAIL_HOST_USER,
                    [sub.users.email],
                )
    course.update = datetime.now(timezone.utc)
    course.save()


@shared_task
def user_deactivation():
    delta = timedelta(days=30)
    users = User.objects.exclude(is_superuser=True)
    now = datetime.now(timezone.utc)
    for user in users:
        if user.last_login and user.is_active:
            if now - user.last_login > delta:
                user.is_active = False
                user.save()
