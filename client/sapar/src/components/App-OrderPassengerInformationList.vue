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
                    :confirm-callback="confirmClick"
                    ref="ticketPerson"
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

import { useVuelidate } from '@vuelidate/core'

export default {
    props: ['orderId'],
    setup() {
        return { v$: useVuelidate() }
    },
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

        confirmClick() {
            let ticketPersons = []

            let isValid = this.$refs.ticketPerson.every((ticketPerson) => {
                
                if(ticketPerson.v$.$invalid) {
                    debugger;
                    let errorMessages = ''
                    ticketPerson.v$.$silentErrors.forEach((error) => {
                        errorMessages+= error.$property + ' ' + error.$message + '<br />'
                    });

                    this.$notify({
                    title: 'Ticket Person with seat: '+ticketPerson.ticket.seatNumber,
                    type: 'error',
                    text: errorMessages
                    })
                    return false
                }
                ticketPersons.push(
                    {
                        'firstName': ticketPerson.form.firstName,
                        'lastName': ticketPerson.form.lastName,
                        'secondName': ticketPerson.form.secondName,
                        'passportNumber': ticketPerson.form.documentNumber,
                        'passportNumberType': ticketPerson.form.documentType,
                        'ticketId': ticketPerson.ticket.id,
                        'cachedPersonId': ticketPerson.form.cachedPerson
                    }
                )
                return true
            })
            
            if(!isValid) return;
            
            let isSuccess = true

            ticketPersons.every((person) => {
                TicketPersonService.create(person).then(
                    (data)=>{
                        
                    },
                    (error)=> {
                        isSuccess = false
                    }
                )

                
                return true
            })

            if(!isSuccess) {
                this.$notify({
                title: 'Ticket Person',
                type: 'error',
                text: 'Failed to save ticket persons'
                })
                return;
            } else {
                
                ticketPersons.every((person) => {
                    let cachedPerson = {
                        cachedPersonId: person.cachedPersonId < 0 ? 0 : person.cachedPersonId,
                        firstName: person.firstName, 
                        lastName: person.lastName,
                        secondName: person.secondName,
                        passportNumberType: person.passportNumberType,
                        passportNumber: person.passportNumber,
                        user: TokenService.getUser().id,
                    }
                    
                    TicketPersonService.saveCachedTicketPerson(cachedPerson).then(
                        (data)=> {
                            console.log("Saved ticket person")
                        },
                        (error)=> {
                            console.log("Failed to save cached Ticket person")
                        }
                    )
                    return true
                })
            }

            this.$router.push({name: 'OrderPayment', params: { orderId: this.order.id }})
        }
    },
    async created() {
        console.log("Mounted Pass Info list")
        await this.getOrderTickets();
        if(this.order == null || TokenService.getUser().id != this.order.user) {
            this.$router.push({'name': 'NotFound'})
        }
        await this.getPassportTypes()
        await this.getCachedTicketPersons();
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