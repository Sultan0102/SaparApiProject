<template>
    <div></div>
    <div v-if="order" id="passanger-info-list">
        <AppOrderPassengerInformation v-for="ticket in order.tickets"
        :key="ticket.id"
        
        />
    </div>
</template>


<script>
import OrderService from '@/services/OrderService';
import AppOrderPassengerInformation from './App-OrderPassengerInformation.vue';

export default {
    props: ['orderId'],
    data() {
        return {
            order: null,
        }
    },
    components: { 
        AppOrderPassengerInformation
    },
    
    methods: {

        async getOrderTickets() {
            await OrderService.retreive(this.orderId).then(
                (data)=> {
                    console.log(data)
                    this.order = data
            }, (err)=> {
                const errorMessage = err.response.data.error_code;

                this.$notify({
                    type: 'error',
                    title: "Order",
                    text: errorMessage || "Error creating order!",
                })
            })
            
        }
    },
    async created() {
        console.log("Mounted")
        console.log(this.orderId);
        await this.getOrderTickets();
        console.log(this.order);
        
    }

}

</script>
