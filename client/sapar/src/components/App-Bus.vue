<template>
       
    <td colspan="3" class="collapse td-schedule" :id="schedule.scheduleNumber">
        <div class="row align-items-center" :id="schedule.scheduleNumber">
                <div class="col-md-9 p-2 my-5 bus-seats mx-auto text-center">
                    <div class ="bus-head my-2 mx-1"></div>
                    <ul v-for="row in formattedTickets" class="list-group list-group-horizontal">
                        <li v-for="ticket in row" 
                        :key="ticket.id" 
                        :class="currentStatusColor(ticket.status)" 
                        @click="occupySeat(ticket)" 
                        class="list-group-item availableSeat m-1 mx-2 text-center flex-wrap mx-auto"
                        >   
                            <span :id=ticket.id>{{ ticket.seatNumber }}</span>
                        </li>
                    </ul>  
                </div>      
                <div class="col-md-3 mx-auto">
                    <div class="mx-auto">
                        <div class="text-start ms-5 ps-5 ms-md-0 ps-md-0 ms-lg-3 ps-lg-3 ms-xl-5 ps-xl-4">
                            <h4 class="mb-4"><span class="colour availableSeat me-2 py-1"></span>{{ $t('Available') }}</h4>
                            <h4 class="mb-4"><span class="colour occupiedSeatByMe me-2 py-1"></span>{{ $t('Occupied') }}</h4>
                            <h4 class="mb-4"><span class="colour bookedSeat me-2 py-1"></span>{{ $t('Booked') }}</h4>
                        </div>
                        <button type="button" class="btn btn-primary my-3 mx-auto col-12" @click="createOrder()">Buy</button>

                        <a @click="pushToTourInfo">
                            <h4>About this tour</h4>
                        </a>
                        <!-- <router-link :to="{
                            name: 'TourInfo',
                            params: { schedule: schedule }
                        }">
                            <h4>About this tour</h4>
                        </router-link> -->
                    </div>
                </div>        
        </div>
    </td>
</template>



<script>
import OrderService from '@/services/OrderService';
import TokenService from '@/services/TokenService';


export default {
    props: ['schedule'],
    data() {
        return {
            tickets: [],
            ticketCounter: 0
        }
    },
    computed: {
        formattedTickets: function() {
            let tickets = [];
            let subTickets = []
            
            for(let i = 0; i < this.tickets.length; i++) {
                if (i % 4 == 0 && i != 0) {
                    tickets.push(subTickets)
                    subTickets = []
                }
                
                // put third 'dummy' element before real ticket
                if(subTickets.length == 2) {
                    subTickets.push({
                        id: null,
                        status: 0
                    })
                }
                
                // let ticket = this.schedule.tickets[i]


                subTickets.push(this.tickets[i])
            }

            return tickets;
        },
        occupiedTickets: function() {
            return this.tickets.filter(t => t.status == 4)
        }
    },
    methods: {
        currentStatusColor(n) {
            switch (n) {
                case 0:
                    return "empty-space";
                case 1:
                    return "bookedSeat";
                case 2:
                    return "bookedSeat";
                case 3:
                    return "availableSeat";
                case 4:
                    return "occupiedSeatByMe";
                default:
                    return "availableSeat";
            }
        },
    
        occupySeat(ticket) {
            if (ticket.id == null || ticket.status == 1 || ticket.status == 2) return;
            
            if (ticket.status == 3) {
                
                if(this.occupiedTickets.length >= 4) {
                    this.$notify({
                        type: 'error',
                        title: "Tickets",
                        text: "You cannot choose more than 4 seats!",
                    })
                    return;
                }
                
                ticket.status = 4;
            } 
            else if (ticket.status == 4) {
                ticket.status = 3;
            }
            
        },


        createOrder() {

            let order = {
                scheduleId: this.schedule.id,
                userId: Number(TokenService.getUser().id),
                ticket_ids: this.occupiedTickets.map(t => t.id)
            }
            
            OrderService.createOrder(order).then((data) => {
                order.id = data.id;
                this.$router.push({params: { orderId: data.id }, name: 'OrderPassengerInformation'})

            }, (error)=> {
                const errorMessage = error.response.data.error_code;

                this.$notify({
                        type: 'error',
                        title: "Order",
                        text: errorMessage || "Error creating order!",
                    })
            })
        },

        pushToTourInfo() {
            console.log(this.schedule)
            debugger;
            // this.$router.push({ name: 'TourInfo', params: { schedule: this.schedule } })
            this.$router.push({ name: 'TourInfo', params: { scheduleId: this.schedule.id } })
        }
    },
    mounted() {
        this.tickets = this.schedule.tickets;
    }

}

</script>



<style scoped>  
*{  
    color: #1C5F41;
}
.bus-head{
    border-style: solid;
    border-width: 2px;
    border-radius: 15px;
    border-bottom-right-radius: 0px;
    border-bottom-left-radius: 0px;
    border-color: #1C5F41;
    height: 90px;
}
.bus-seats{
    border-style: solid;
    border-width: 2px;
    border-radius: 20px;
    max-width: 330px !important;
    border-color: #1C5F41;
}
.list-group-item{
  border-width: 2px !important;
  border-color: #1C5E3C;
  border-radius: 17px !important;
  width: 46.2px !important;
  color: #1C5E3C;
  font-size: 26px;
  padding: .1rem .1rem !important;
}
.availableSeat{
    background-color: #FFF;
    cursor: pointer;
}
.occupiedSeatByMe{
    background-color: #D5D4D4;
    cursor: default;
}
.bookedSeat{
    background-color: #57896F;
    color: #FFF !important;
    cursor: pointer;
}
.empty-space{
    opacity: 0;
    cursor: default;
    height: 42px;
    width: 25px !important;
}
.collapse, .collapsing{
    background-color: #FFF;
    padding: 0 !important;
    margin: 0 !important;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}

select{
    background-color:#FFF !important;
}
.colour{
    padding-left: 37px;
    border-width: 2px !important;
    border-color: #1C5E3C !important;
    border-radius: 15px !important;
    border-style: solid !important;
    cursor: default;
}
a{
    color: #1C5F41 !important;
    text-decoration: underline !important;
}

</style>