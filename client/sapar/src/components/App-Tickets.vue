<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="col-xxl-8 col-10 mx-auto mb-3">
            <div class="input-group mx-auto">
                <input type="search" class="form-control" placeholder="From:" aria-label="Search">
                <input type="search" class="form-control" placeholder="To:" aria-label="Search">
                <div class="form-control"><VueDatePicker  v-model="date" model-auto range position="right"/></div>
                <button class="btn search" type="button"><i class="bi bi-search"></i></button>
            </div>
        </div>
        <div class="container table-responsive">
            <table class="table table-hover text-center">
                <thead>
                    <tr>
                        <th scope="col">{{ $t('Route') }}<i class="bi bi-filter ms-1"></i></th>
                        <th scope="col">{{ $t('From - To') }}<i class="bi bi-filter ms-1"></i></th>
                        <th scope="col">{{ $t('Departure - Arrival Time') }}<i class="bi bi-filter ms-1"></i></th>
                    </tr>
                </thead>
                <tbody>
                    <tr data-bs-toggle="collapse" data-bs-target="#bus2">
                        <th scope="row">AB4958</th>
                        <td>Almaty - Taraz</td>
                        <td>10:40pm - 05:30pm</td>
                    </tr>   
                    <td colspan="3" class="collapse" id="bus2">
                        <div class="row align-items-center " id="bus2">
                                    <div class="col-8 p-2 my-5 bus-seats mx-auto">
                                        <div class="list-group list-group-horizontal flex-wrap">
                                            <div v-for="ticket in tickets" :class="currentStatusColor(ticket.ticketStatus)" @click="occupySeat(ticket)" class="list-group-item availableSeat m-1 mx-2 text-center">
                                                <span>{{ ticket.seatNumber }}</span>
                                            </div>
                                        </div>  
                                    </div>      
                                    <div class="col-4 mx-auto">
                                            <h6 class="mb-0 mb-md-3">Available</h6>
                                            <h6 class="mb-0 mb-md-3">Occupied</h6>
                                            <h6 class="mb-0 mb-md-3">Booked</h6>
                                            <button type="button" class="btn btn-primary mx-auto my-3">Buy</button>
                                    </div>        
                        </div>
                    </td>

                    <!-- <tr data-bs-toggle="collapse" data-bs-target="#bus3">
                        <th scope="row">AB4958</th>
                        <td>Almaty - Taraz</td>
                        <td>10:40pm</td>
                    </tr>
                                    
                    <td colspan="3" class="collapse " id="bus3">
                        <div class="row align-items-center " id="bus3">
                                <div class="col-md-9 p-2 my-5 bus-seats mx-auto text-center">
                                    <ul v-for="row in tickets" class="list-group list-group-horizontal">
                                        <li v-for="ticket in row" :key="ticket.id" :class="currentStatusColor(ticket.ticketStatus)" @click="occupySeat(ticket)" class="list-group-item availableSeat m-1 mx-2 text-center flex-wrap">
                                            <span>{{ ticket.seatNumber }}</span>
                                        </li>
                                    </ul>  
                                </div>      
                                <div class="col-md-3 mx-auto">
                                        <h6 class="mb-3 py-3 colour mx-auto availableSeat">Available</h6>
                                        <h6 class="mb-3 py-3 colour mx-auto occupiedSeat">Occupied</h6>
                                        <h6 class="mb-3 py-3 colour mx-auto bookedSeat">Booked</h6>
                                        <button type="button" class="btn btn-primary mx-auto my-3">Buy</button>
                                </div>        
                        </div>
                    </td> -->
                    
                    <AppBus />
                </tbody>
            </table>
        </div>
    </div>

</template>

<script>
import TicketService from "@/services/TicketService"
import AppBus from "@/components/App-Bus.vue";

export default{
    name: "Tickets",
    components: {
        AppBus
    },
    data() {
        return {
            schedules: null
        };
    },
    methods: {
        
    },
    mounted() {
        
    },
    components: { AppBus }
}
</script>

<style scoped>  
*{
	color: #1C5E3C;
}
 th{
    padding-bottom: 1rem !important;
    min-width: 33.3% !important;
}
.form-control, .form-control-plaintext{
    border-bottom: none !important;
    border-radius: 15px;
    max-width: 40% !important;
}

.collapse, .collapsing{
    background-color: #FFF;
    padding: 0 !important;
    margin: 0 !important;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}
.search{
    border-bottom-right-radius: 15px !important;
	border-top-right-radius: 15px !important;
    background-color: #FFF !important;
}
.input-group{
    max-width: 1300px;
}
</style>