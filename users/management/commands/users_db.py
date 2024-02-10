from django.core.management import BaseCommand

from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@mail.ru',
            first_name='Test',
            last_name='Testov',
        )
        user.set_password('Test1234')
        user.save()

        user = User.objects.create(
            email='test1@mail.ru',
            first_name='Test1',
            last_name='Testov1',
        )
        user.set_password('Test4321')
        user.save()

        user = User.objects.create(
            email='moderator@mail.ru',
            first_name='Moderator',
            last_name='Moderatorov',
        )
        user.set_password('Mod4321')
        user.save()

        payment = Payment.objects.create(
            user_id=3,
            date_of_payment='2023-10-05',
            paid_course_id=2,
            payment_amount=2500,
            payment_method='cash',
        )
        payment.save()

        payment = Payment.objects.create(
            user_id=3,
            date_of_payment='2023-11-15',
            paid_course_id=3,
            payment_amount=3000,
            payment_method='non-cash',
        )
        payment.save()

        payment = Payment.objects.create(
            user_id=4,
            date_of_payment='2023-12-15',
            paid_course_id=3,
            payment_amount=3000,
            payment_method='cash',
        )
        payment.save()
