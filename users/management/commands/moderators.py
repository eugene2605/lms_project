from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        Group.objects.create(name='moderators')

        user = User.objects.create(
            email='moderator@mail.ru',
            first_name='Moderator',
            last_name='Moderatorov',
            is_staff=True,
        )
        user.set_password('Mod4321')
        moderators = Group.objects.get(name="moderators")
        user.groups.add(moderators)
        user.save()
