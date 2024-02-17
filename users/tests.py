from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User, Payment


class UsersTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='Admin', password='admin', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title='Test', description='Test')

    def test_create_user(self):
        """Тестирование создания пользователя"""
        data = {'email': 'Test@mail.ru', 'password': 'Test'}
        response = self.client.post('/user/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.all().exists())

    def test_list_user(self):
        """Тестирование вывода списка пользователей"""
        user = User.objects.create(email='List_test@mail.ru', password='List_test')
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(user, User.objects.all())

    def test_retrieve_user(self):
        """Тестирование вывода одного пользователя"""
        user2 = User.objects.create(email='Retrieve_test@mail.ru', password='Retrieve_test')
        response = self.client.get(f'/user/{user2.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(user2, User.objects.all())

    def test_update_user(self):
        """Тестирование изменения пользователя"""
        # user3 = User.objects.create(email='Update_test@mail.ru', password='Update_test')
        update = {'password': 'Update'}
        response = self.client.patch(f'/user/update/{self.user.pk}/', update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user, User.objects.all())
        # self.assertEqual(response.json().get('email'), 'Update@mail.ru')
        self.assertEqual(response.json().get('password'), 'Update')

    def test_delete_user(self):
        """Тестирование удаления пользователя"""
        user4 = User.objects.create(email='Delete_test@mail.ru', password='Delete_test')
        response = self.client.delete(f'/user/delete/{user4.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(not User.objects.filter(pk=user4.pk).exists())

    def test_create_payment(self):
        """Тестирование создания оплаты"""
        data = {'user': self.user.pk, 'date_of_payment': '2024-02-15', 'paid_course': self.course.pk,
                'payment_amount': 1500, 'payment_method': 'cash'}
        response = self.client.post('/user/payment/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Payment.objects.all().exists())
        self.assertEqual(response.json(),
                         {'id': 1, 'date_of_payment': '2024-02-15', 'payment_amount': 1500.0,
                          'payment_method': 'cash', 'user': 12, 'paid_course': 7}
                         )

    def test_list_payment(self):
        """Тестирование вывода списка оплат"""
        payment = Payment.objects.create(user=self.user, date_of_payment='2024-02-02', paid_course=self.course,
                                         payment_amount=2500, payment_method='non-cash')
        response = self.client.get('/user/payment/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(payment, Payment.objects.all())

    def test_retrieve_payment(self):
        """Тестирование вывода одной оплаты"""
        payment2 = Payment.objects.create(user=self.user, date_of_payment='2024-01-12', paid_course=self.course,
                                          payment_amount=5500, payment_method='non-cash')
        response = self.client.get(f'/user/payment/{payment2.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(payment2, Payment.objects.all())

    def test_update_payment(self):
        """Тестирование изменения оплаты"""
        payment3 = Payment.objects.create(user=self.user, date_of_payment='2023-11-12', paid_course=self.course,
                                          payment_amount=8500, payment_method='cash')
        update = {'date_of_payment': '2023-12-02', 'payment_method': 'non-cash'}
        response = self.client.patch(f'/user/payment/update/{payment3.pk}/', update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(payment3, Payment.objects.all())
        self.assertEqual(response.json().get('date_of_payment'), '2023-12-02')
        self.assertEqual(response.json().get('payment_method'), 'non-cash')

    def test_delete_payment(self):
        """Тестирование удаления оплаты"""
        payment4 = Payment.objects.create(user=self.user, date_of_payment='2023-10-25', paid_course=self.course,
                                          payment_amount=8500, payment_method='non-cash')
        response = self.client.delete(f'/user/payment/delete/{payment4.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(not Payment.objects.all().exists())
