<template>
    <div class="container-fluid mt-lg-2 mt-1">
        <div class="container">
            <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
            </div>
            <div class="carousel-inner mb-3 pb-5">
                <div class="carousel-item active" data-bs-interval="100000000000">
                    <div class="container-fluid">
                        <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
                            <form class="text-center mt-5 mx-auto">
                                <h2 class="pt-3">{{ $t('Order confirmation') }}</h2>
                                <div class="mt-3 py-4">
                                    <select class="mx-auto form-select">
                                        <option selected disabled class="selected">{{ $t('Choose passengers') }}</option>
                                        <option value="1" data-content="">Vasya Pupkin</option>
                                        <option value="2">Anatoliy Pupkin</option>
                                        <option value="3">{{ $t('Add a new passenger') }}</option>
                                    </select>
                                </div>
                                <h2 class="pt-3">{{ $t('Passenger Information') }}</h2>
                                <div class="mb-3">
                                    <input disabled type="firstname" class="form-control mx-auto disabled" id="firstname" placeholder="Vasia">
                                </div>
                                <div class="mb-3">
                                    <input disabled type="lastname" class="form-control mx-auto disabled" id="lastname" placeholder="Pupkin">
                                </div>
                                <div class="mb-3">
                                    <input disabled type="lastname" class="form-control mx-auto disabled" id="lastname" placeholder="Poluektovich">
                                </div>
                                <select disabled class="mx-auto form-select mb-3 disabled">
                                    <option selected disabled class="selected">{{ $t('Document Type') }}</option>
                                    <option value="1" data-content="">{{ $t('Passport') }}</option>
                                    <option value="2">{{ $t('Identity Card') }}</option>
                                </select>   
                                <div class="mb-3">
                                    <input disabled type="lastname" class="form-control mx-auto disabled" id="lastname" placeholder="Document Number">
                                </div>
                                <button type="submit" class="btn btn-primary my-3" data-bs-target="#carouselExampleDark" data-bs-slide="next">{{ $t('Next') }}</button><br/>
                                <button disabled type="submit" class="btn btn-primary mt-3 mb-5">{{ $t('Confirm') }}</button>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="carousel-item" data-bs-interval='100000000000'>
                    <div class="container-fluid">
                        <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
                            <form class="text-center mt-5 mx-auto">
                                <h2 class="pt-3">{{ $t('Order confirmation') }}</h2>
                                <div class="mt-3 py-4">
                                    <select class="mx-auto form-select">
                                        <option selected disabled class="selected">{{ $t('Choose passengers') }}</option>
                                        <option value="1" data-content="">Vasya Pupkin</option>
                                        <option value="2">Anatoliy Pupkin</option>
                                        <option value="3">{{ $t('Add a new passenger') }}</option>
                                    </select>
                                </div>
                                <h2 class="pt-3">{{ $t('Passenger Information') }}</h2>
                                <div class="mb-3">
                                    <input disabled type="firstname" class="form-control mx-auto disabled" id="firstname" placeholder="Vasia">
                                </div>
                                <div class="mb-3">
                                    <input disabled type="lastname" class="form-control mx-auto disabled" id="lastname" placeholder="Pupkin">
                                </div>
                                <div class="mb-3">
                                    <input disabled type="lastname" class="form-control mx-auto disabled" id="lastname" placeholder="Poluektovich">
                                </div>
                                <select disabled class="mx-auto form-select mb-3 disabled">
                                    <option selected disabled class="selected">{{ $t('Document Type') }}</option>
                                    <option value="1" data-content="">{{ $t('Passport') }}</option>
                                    <option value="2">{{ $t('Identity Card') }}</option>
                                </select>   
                                <div class="mb-3">
                                    <input disabled type="lastname" class="form-control mx-auto disabled" id="lastname" placeholder="Document Number">
                                </div>
                                <button type="submit" class="btn btn-primary my-3" data-bs-target="#carouselExampleDark" data-bs-slide="prev">{{ $t('Previous') }}</button><br/>
                                <button disabled type="submit" class="btn btn-primary mt-3 mb-5">{{ $t('Confirm') }}</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
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