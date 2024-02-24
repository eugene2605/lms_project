from rest_framework import serializers

from users.models import User, Payment
from users.services import create_obj_payment, create_obj_price, create_session_pay


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentCreateSerializers(serializers.ModelSerializer):
    payment_link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'

    def get_payment_link(self, instance):
        course_name = f'Оплата курса {instance.paid_course.title} от {instance.user.email}'
        course_id = create_obj_payment(course_name)
        price = instance.payment_amount
        price_id = create_obj_price(course_id, price)
        payment_link = create_session_pay(price_id)
        return payment_link


class UserFullSerializers(serializers.ModelSerializer):
    payment = PaymentSerializers(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserGeneralSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar')
