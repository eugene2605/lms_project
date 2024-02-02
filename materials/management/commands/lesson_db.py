from django.core.management import BaseCommand

from materials.models import Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        lesson = Lesson.objects.create(
            title='ORM',
            description='Work in database',
            course_id=2
        )
        lesson.save()

        lesson = Lesson.objects.create(
            title='Templateization',
            description='Work in templates',
            course_id=2
        )
        lesson.save()

        lesson = Lesson.objects.create(
            title='FBV and CBV',
            description='Work in views',
            course_id=2
        )
        lesson.save()

        lesson = Lesson.objects.create(
            title='ViewSet and Generic',
            description='Work in APIViews',
            course_id=3
        )
        lesson.save()

        lesson = Lesson.objects.create(
            title='Serializers',
            description='Working with data serialization',
            course_id=3
        )
        lesson.save()
