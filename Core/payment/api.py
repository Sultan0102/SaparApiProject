from rest_framework import viewsets
from Core.payment.models import Payment
from Core.payment.serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ]




