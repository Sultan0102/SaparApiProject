from rest_framework import serializers
from Core.payment.models import Payment
from Core.tickets.models import Order, Ticket
from django.db.transaction import atomic
from Core.exceptions import FailedToCreatePayment


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'
    
    @atomic
    def create(self, validated_data):
        try:
            payment = Payment.objects.create(**validated_data)
            
            order = Order.objects.get(id=payment.order.id)
            order.isPaid = True
            order.save()

            tickets = Ticket.objects.filter(order__id=order.id)
            tickets.update(status_id=2); 

        except Exception:
            raise FailedToCreatePayment()

        return payment