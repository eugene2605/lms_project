# Generated by Django 4.2.10 on 2024-03-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_course_update_lesson_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='update',
        ),
        migrations.AlterField(
            model_name='course',
            name='update',
            field=models.DateTimeField(default=None, verbose_name='последнее обновление'),
        ),
    ]
