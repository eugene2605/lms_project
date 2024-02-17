from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='Test', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

    def test_create_course(self):
        """Тестирование создания курса"""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.client.post('/course/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Course.objects.all().exists())
        self.assertEqual(response.json(),
                         {'id': 1, 'lesson_count': 0, 'lesson': [], 'subscription': False, 'title': 'Test',
                          'preview': None, 'description': 'Test', 'owner': None}
                         )

    def test_list_course(self):
        """Тестирование вывода списка курсов"""
        course = Course.objects.create(title='List_test', description='List_test')
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(course, Course.objects.all())

    def test_retrieve_course(self):
        """Тестирование вывода одного курса"""
        course2 = Course.objects.create(title='Retrieve_test', description='Retrieve_test')
        response = self.client.get(f'/course/{course2.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(course2, Course.objects.all())

    def test_update_course(self):
        """Тестирование изменения курса"""
        course3 = Course.objects.create(title='Update_test', description='Update_test')
        update = {'title': 'Update', 'description': 'Update'}
        response = self.client.put(f'/course/update/{course3.pk}/', update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(course3, Course.objects.all())
        self.assertEqual(response.json().get('title'), 'Update')
        self.assertEqual(response.json().get('description'), 'Update')

    def test_delete_course(self):
        """Тестирование удаления курса"""
        course4 = Course.objects.create(title='Delete_test', description='Delete_test')
        response = self.client.delete(f'/course/delete/{course4.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(not Course.objects.all().exists())

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.client.post('/lesson/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.all().exists())
        self.assertEqual(response.json(),
                         {'id': 1, 'title': 'Test', 'description': 'Test', 'preview': None,
                         'link': None, 'course': None, 'owner': None}
                         )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""
        lesson = Lesson.objects.create(title='List_test', description='List_test')
        response = self.client.get('/lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(lesson, Lesson.objects.all())

    def test_retrieve_lesson(self):
        """Тестирование вывода одного урока"""
        lesson2 = Lesson.objects.create(title='Retrieve_test', description='Retrieve_test')
        response = self.client.get(f'/lesson/{lesson2.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(lesson2, Lesson.objects.all())

    def test_update_lesson(self):
        """Тестирование изменения урока"""
        lesson3 = Lesson.objects.create(title='Update_test', description='Update_test')
        update = {'title': 'Update', 'description': 'Update'}
        response = self.client.put(f'/lesson/update/{lesson3.pk}/', update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(lesson3, Lesson.objects.all())
        self.assertEqual(response.json().get('title'), 'Update')
        self.assertEqual(response.json().get('description'), 'Update')

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        lesson4 = Lesson.objects.create(title='Delete_test', description='Delete_test')
        response = self.client.delete(f'/lesson/delete/{lesson4.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(not Lesson.objects.all().exists())

    def test_subscription(self):
        """Тестирование подписки на курс"""
        course5 = Course.objects.create(title='Sub_test', description='Sub_test')
        data = {'user': self.user, 'course_id': course5.id}
        response = self.client.post('/course/sub/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.all().exists())
        response = self.client.post('/course/sub/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(not Subscription.objects.all().exists())
