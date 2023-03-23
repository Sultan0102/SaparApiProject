<template>
    <div class="container-fluid mt-lg-2 mt-1">
        <div class="container">
            <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel" data-bs-interval="false">
                
                <div v-if="order" class="carousel-inner mb-3 pb-5">
                    <AppOrderPassengerInformation v-for="(ticket, index) in order.tickets"
                    :key="ticket.id"
                    :class="index==0 ? 'active': ''"
                    :ticket="ticket"
                    :cachedTicketPersons="cachedTicketPersons"
                    :passportTypes="documentTypes"
                    :index="index"
                    :isLast="index == order.tickets.length-1"
                    />
                    
                    <div class="carousel-indicators">
                        <button v-for="(ticket, index) in order.tickets"
                         type="button" 
                         data-bs-target="#carouselExampleDark"
                         :data-bs-slide-to="index"
                         :key="index"
                         :class="index ==0 ? 'active': ''"
                         aria-current="true"
                         aria-label="Slide 1">
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import OrderService from '@/services/OrderService';
import AppOrderPassengerInformation from './App-OrderPassengerInformation.vue';
import TokenService from '@/services/TokenService';
import TicketService from '@/services/TicketService';
import TicketPersonService from '@/services/TicketPersonService';


export default {
    props: ['orderId'],
    data() {
        return {
            order: null,
            cachedTicketPersons: [],
            documentTypes: [],
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
            
        },

        async getPassportTypes() {
            await TicketService.getPassportTypes().then(
                (data)=> {
                    this.documentTypes = data
                }
            )
        },

        async getCachedTicketPersons() {

            await TicketPersonService.getCachedTicketPerson(TokenService.getUser().id).then(
                (data)=> {
                    this.cachedTicketPersons = data
                }
            )
        },
        enableValidation() {
            // on all the forms(differentiate by id: ticket-person-form- + ticket.id)
        }
    },
    async created() {
        console.log("Mounted")
        await this.getOrderTickets();
        console.log(TokenService.getUser())
        if(this.order == null || TokenService.getUser().id != this.order.user) {
            this.$router.push({'name': 'NotFound'})
        }
        await this.getPassportTypes()
        await this.getCachedTicketPersons();
        console.log(this.order);
        console.log(this.documentTypes);
        console.log(this.cachedTicketPersons);
    }

}

</script>


<style scoped>
.bi-caret-left-fill, .bi-caret-right-fill{
	color: #1C5E3C !important;
    font-size: 48px;
}
.disabled{
    opacity: 0.5;
}
.btn-primary{
    min-width: 250px;
}
</style>