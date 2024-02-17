from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserFullSerializers(serializers.ModelSerializer):
    payment = PaymentSerializers(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserGeneralSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar')
