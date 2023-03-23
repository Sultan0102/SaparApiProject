<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-5">
                <h2 class="pt-3">{{ $t('Order confirmation') }}</h2>

                <div class="dropdown mt-3">
                    <button class="btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                        {{ $t('Choose passangers') }}
                    </button>
                    <ul class="dropdown-menu">
                        <li v-for="cachedTicketPerson in cachedTicketPersons" 
                        :key="cachedTicketPerson.id"
                        >
                            <a class="dropdown-item" href="#">{{ cachedTicketPerson.firstName }} {{ cachedTicketPerson.lastName }} <i class="bi bi-pencil-square"></i></a>
                        </li>
                        
                        <li><a class="dropdown-item" href="#" >{{ $t('Add a new passenger') }}</a></li>
                    </ul>
                </div>
                <button type="submit" class="btn btn-primary mt-3 mb-3" @click="clickPassengerOption()">{{ $t('Next') }}</button> <br/>
            </form>
        </div>
    </div>
</template>


<script>
import OrderService from "@/services/OrderService";
import TicketPersonService from "@/services/TicketPersonService"
import TicketService from "@/services/TicketService";
import { thisTypeAnnotation } from "@babel/types";

export default {
    props: ['id'],

    data() {
        return {
            cachedTicketPersons: [],
            passengerOption: 0,
            order: null,
            tickets: []
        }
    },
    methods: {
        getCachedPersons() {
            TicketPersonService.getCachedTicketPerson().then(
                (data)=> {
                    this.cachedTicketPersons = data;
                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: "Error",
                        text: error.response.data.error_code,
                    })
                }
            )
        },

        async getOrderAndTickets() {
            let o = null
            let tickets = []

            await OrderService.retreive(this.id).then(
                (order)=> {
                    debugger;
                    o = order
                    tickets = order.tickets
                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: "Error",
                        text: error.response.data.error_code,
                    })
                }
            )

            this.order = o
            this.tickets = tickets;
        },


        clickPassengerOption() {
            console.log("Option")
            console.log(this.passengerOption)
        }
        
    },
    mounted() {
        console.log("Order Mounted")
        this.getOrderAndTickets();
        console.log(this.order)
        this.getCachedPersons(this.order.user);

    }
}

</script>

<style scoped>
p{
    color:#1C5E3C;
    padding-bottom: 0px !important;
}
.alert{
    margin: auto;
    width: 50%;
}
form{
	max-width: 600px;
}
.btn-secondary {
  color: #6c757d !important;
  background-color: #fff;
  border: none !important;
  border-color: #1C5E3C;
  border-bottom: 1px solid !important;
}
.btn-check:focus + .btn-secondary, .btn-secondary:focus {
  box-shadow: none !important;
}
.dropdown-item{
    color: #1C5E3C !important;
}
</style>