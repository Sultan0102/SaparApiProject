from rest_framework import serializers
from Core.payment.models import Payment
from Core.tickets.models import Order, Ticket
from django.db.transaction import atomic
from Core.exceptions import FailedToCreatePayment
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Core.settings import BASE_DIR

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'
    
    @atomic
    def create(self, validated_data):
        print(BASE_DIR)
        try:
            payment = Payment.objects.create(**validated_data)
            
            order = Order.objects.get(id=payment.order.id)
            order.isPaid = True
            order.save()

            tickets = Ticket.objects.filter(order__id=order.id)
            tickets.update(status_id=2); 

        except Exception:
            raise FailedToCreatePayment()
        
        ctx = {
            'orderNumber': 3546520110,
            'seatNumber': tickets[0].seatNumber,
            'firstName': order.user.firstName,
            'lastName': order.user.lastName,
        }

        html_message=render_to_string('payment.html', context=ctx)
        try:
            send_mail(
                subject="Payment Confirmation",
                message=strip_tags(html_message),
                html_message=html_message,
                from_email="saparServicePass@yandex.ru",
                recipient_list=[payment.user.email],
                fail_silently=False
            )
        except Exception as e:
            print(e)
            raise FailedToCreatePayment

        return payment