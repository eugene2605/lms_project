from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    payment = PaymentSerializers(many=True)

    class Meta:
        model = User
        fields = '__all__'
