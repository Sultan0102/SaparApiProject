<template>
    <div class="container-fluid my-5 py-5">
        <div class="container mt-lg-5 mt-4 pt-lg-5 pt-4">
            <form id="order-payment-form" class="text-center mt-5 mx-auto" @submit.prevent="createPayment">
                <h2 class="pt-3">{{ $t('Checkout Details') }}</h2>
                <div class="mt-3 py-4">
                    
                    <select v-model="selectedMethod" id="orderPaymentMethods" name="orderPaymentMethods" class="mx-auto form-select mb-5">
                        <option disabled selected class="selected" value="0">{{ $t('Payment Method') }} </option>
                        <option value="1">Kaspi</option>
                        <option value="2">Halyk</option>
                        <!-- <option v-for="paymentMethod in paymentMethods"
                        :key="paymentMethod.id"
                        :value="paymentMethod.id"
                        >
                        {{ paymentMethod.name }} -->
                        <!-- </option> -->
                    </select>
                </div>
                <button type="submit" class="btn btn-primary my-5">{{ $t('Confirm') }}</button>
            </form>
        </div>
    </div>
</template>


<script>
import OrderService from '@/services/OrderService';
import PaymentService from '@/services/PaymentService';
import TokenService from '@/services/TokenService';


export default {
    props: ['orderId'],
    data() {
        return {
            order: null,
            paymentMethods: [
                {
                    id: 1,
                    name: 'Kaspi',
                },
                {
                    id: 2,
                    name: 'Halyk',
                },
            ],
            selectedMethod: 0
        }
    },
    methods: {
        async getOrder() {
            let o = null
            await OrderService.retreive(this.orderId).then(
                (order)=> {
                    o = order
                },
                (error)=> {
                    debugger;
                    this.$notify({
                        type: 'error',
                        title: "Error",
                        text: error.response.data.error_code,
                    })
                }
            )
            this.order = o;
        },
        getCurrentFormattedDate() {
            const timeElapsed = Date.now();
            const today = new Date(timeElapsed);

            const formattedToday = today.toISOString();

            return formattedToday;
        },
        createPayment() {
            debugger;

            if(this.selectedMethod == 0) {
                this.$notify({
                    title: "Validation Error",
                    type: 'error',
                    text: 'You have to choose payment method!'
                })
            }

            const selectedMethodName = this.paymentMethods.filter(p => p.id == this.selectedMethod)[0].name;
            const formattedDate = this.getCurrentFormattedDate();
            const payment = {
                method: selectedMethodName,
                payDate: formattedDate,
                paymentAmount: this.order.totalPrice,
                orderId: this.order.id,
                userId: TokenService.getUser().id
            }

            PaymentService.createPayment(payment).then(
                (data)=> {
                    this.$router.push({name: 'OrderNumber'})
                },
                (error)=> {
                    this.$notify({
                        title: "Payment Error",
                        type: 'error',
                        text: 'Failed to create Payment!'
                    })
                }
            )

        }
    },
    mounted() {
        this.getOrder();

    }
}
</script>

<style scoped>

</style>