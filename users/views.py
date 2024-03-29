from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from users.models import User, Payment
from users.permissions import IsSuperUser, IsOwner
from users.serializers import PaymentSerializers, UserFullSerializers, UserGeneralSerializers, PaymentCreateSerializers


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserFullSerializers
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return UserFullSerializers
        return UserGeneralSerializers


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser or self.request.user.email == self.get_object().email:
            return UserFullSerializers
        return UserGeneralSerializers


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserFullSerializers
    queryset = User.objects.all()
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsSuperUser | IsOwner]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentCreateSerializers

    def perform_create(self, serializer):
        new_pay = serializer.save(user=self.request.user)
        new_pay.save()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ('date_of_payment',)
    filterset_fields = ('paid_course', 'payment_method')


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
