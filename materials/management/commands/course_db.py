from django.core.management import BaseCommand

from materials.models import Course


class Command(BaseCommand):

    def handle(self, *args, **options):
        course = Course.objects.create(
            title='Django',
            description='Most popular framework',
        )
        course.save()

        course = Course.objects.create(
            title='DRF',
            description='Django-package for work with API',
        )
        course.save()
