<template>
    <div class="container-fluid py-5 mt-5">
        <div class="col-xl-6 mx-auto mb-3">
            <input type="search" class="form-control" placeholder="Search here" aria-label="Search">
        </div>
        <div class="container table-responsive">
            <table class="table table-hover text-center">
                <thead>
                    <tr>
                        <th scope="col">{{ $t('     Route    ') }}</th>
                        <th scope="col">{{ $t('   From - To  ') }}</th>
                        <th scope="col">{{ $t('Departure - Arrival Time') }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr data-bs-toggle="collapse" data-bs-target="#bus2">
                        <th scope="row">AB4958</th>
                        <td>Almaty - Taraz</td>
                        <td>10:40pm - 05:30pm</td>
                    </tr>   
                    <td colspan="3" class="collapse " id="bus2">
                        <div class="row align-items-center " id="bus2">
                                    <div class="col-6 p-2 my-5 bus-seats mx-auto">
                                        <ul class="list-group list-group-horizontal flex-wrap">
                                            <li v-for="ticket in tickets" :class="currentStatusColor(ticket.ticketStatus)" @click="occupySeat(ticket)" class="list-group-item availableSeat m-1 mx-2 text-center">
                                                <span>{{ ticket.seatNumber }}</span>
                                            </li>
                                        </ul>  
                                    </div>      
                                    <div class="col-3 mx-auto">
                                            <h6 class="mb-0 mb-md-3">Available</h6>
                                            <h6 class="mb-0 mb-md-3">Occupied</h6>
                                            <h6 class="mb-0 mb-md-3">Booked</h6>
                                            <button type="button" class="btn btn-primary mx-auto my-3">Buy</button>
                                    </div>        
                        </div>
                    </td>
                    <tr data-bs-toggle="collapse" data-bs-target="#bus3">
                        <th scope="row">AB4958</th>
                        <td>Almaty - Taraz</td>
                        <td>10:40pm</td>
                    </tr>   
                    <td colspan="3" class="collapse " id="bus3">
                        <div class="row align-items-center " id="bus3">
                                    <div class="col-6 p-2 my-5 bus-seats mx-auto">
                                        <ul class="list-group list-group-horizontal flex-wrap">
                                            <li v-for="ticket in tickets" :class="currentStatusColor(ticket.ticketStatus)" @click="occupySeat(ticket)" class="list-group-item availableSeat m-1 mx-2 text-center">
                                                <span>{{ ticket.seatNumber }}</span>
                                            </li>
                                        </ul>  
                                    </div>      
                                    <div class="col-3 mx-auto">
                                            <h6 class="mb-0 mb-md-3">Available</h6>
                                            <h6 class="mb-0 mb-md-3">Occupied</h6>
                                            <h6 class="mb-0 mb-md-3">Booked</h6>
                                            <button type="button" class="btn btn-primary mx-auto my-3">Buy</button>
                                    </div>        
                        </div>
                    </td>
                </tbody>
            </table>
        </div>
    </div>

</template>

<script>
import TicketService from "@/services/TicketService"

export default{

    data(){
        return{
            tickets:[
            { id: 1, seatNumber: 1, ticketStatus: 1},
            { id: 2, seatNumber: 2, ticketStatus: 2},
            { id: 3, seatNumber: 3, ticketStatus: 1},
            { id: 4, seatNumber: 4, ticketStatus: 2},
            { id: 5, seatNumber: 5, ticketStatus: 1},
            { id: 6, seatNumber: null, ticketStatus: 0},
            { id: 7, seatNumber: 6, ticketStatus: 2},
            { id: 8, seatNumber: 7, ticketStatus: 1},
            { id: 9, seatNumber: 8, ticketStatus: 2},
            { id: 10, seatNumber: 9, ticketStatus: 1},
            { id: 11, seatNumber: 10, ticketStatus: 2},
            { id: 12, seatNumber: 11, ticketStatus: 1},
            { id: 13, seatNumber: 12, ticketStatus: 2},
            { id: 14, seatNumber: 13, ticketStatus: 1},
            { id: 15, seatNumber: 14, ticketStatus: 2},
            { id: 16, seatNumber: 15, ticketStatus: 1},
            { id: 17, seatNumber: null, ticketStatus: 0},
            { id: 18, seatNumber: 16, ticketStatus: 2},
            { id: 19, seatNumber: 17, ticketStatus: 1},
            { id: 20, seatNumber: 18, ticketStatus: 2},
            { id: 21, seatNumber: 19, ticketStatus: 1},
            { id: 22, seatNumber: 20, ticketStatus: 2},
            { id: 23, seatNumber: null, ticketStatus: 0},
            { id: 24, seatNumber: null, ticketStatus: 0},
            { id: 25, seatNumber: null, ticketStatus: 0},
            { id: 26, seatNumber: null, ticketStatus: 0},
            { id: 27, seatNumber: null, ticketStatus: 0},
            { id: 28, seatNumber: null, ticketStatus: 0},
            { id: 29, seatNumber: null, ticketStatus: 0},
            { id: 30, seatNumber: null, ticketStatus: 0},
            { id: 31, seatNumber: null, ticketStatus: 0},
            { id: 32, seatNumber: null, ticketStatus: 0},
            { id: 33, seatNumber: null, ticketStatus: 0},
            { id: 34, seatNumber: 21, ticketStatus: 2},
            { id: 35, seatNumber: 22, ticketStatus: 1},
            { id: 36, seatNumber: 23, ticketStatus: 2},
            { id: 37, seatNumber: 24, ticketStatus: 1},
            { id: 38, seatNumber: 25, ticketStatus: 2},
            { id: 39, seatNumber: null, ticketStatus: 0},
            { id: 40, seatNumber: 26, ticketStatus: 2},
            { id: 41, seatNumber: 27, ticketStatus: 1},
            { id: 42, seatNumber: 28, ticketStatus: 2},
            { id: 43, seatNumber: 29, ticketStatus: 1},
            { id: 44, seatNumber: 30, ticketStatus: 2},
            { id: 45, seatNumber: 31, ticketStatus: 1},
            { id: 46, seatNumber: 32, ticketStatus: 2},
            { id: 47, seatNumber: 33, ticketStatus: 1},
            { id: 48, seatNumber: 34, ticketStatus: 2},
            { id: 49, seatNumber: 35, ticketStatus: 1},
            { id: 50, seatNumber: null, ticketStatus: 0},
            { id: 51, seatNumber: 36, ticketStatus: 2},
            { id: 52, seatNumber: 37, ticketStatus: 1},
            { id: 53, seatNumber: 38, ticketStatus: 2},
            { id: 54, seatNumber: 39, ticketStatus: 1},
            { id: 55, seatNumber: 40, ticketStatus: 2}
            ],
            ticketsSum: 0
        }
    },
    methods:{
        currentStatusColor(n){
            switch(n){
                    case 0:
                        return 'empty-space';
                    case 1:
                        return 'availableSeat';
                    case 2:
                        return 'occupiedSeat';
                    case 3:
                        return 'bookedSeat';
            }
        },
        occupySeat(ticket){
            if (ticket.ticketStatus == 1 && this.ticketsSum < 5) {
                ticket.ticketStatus = 3
                this.ticketsSum++
            } 
            else if(ticket.ticketStatus == 3){
                ticket.ticketStatus = 1
                this.ticketsSum--
            }
            else {
                console.log(ticket.ticketStatus)
            }
            console.log(this.ticketsSum)
        },
        getTickets(){
            TicketService.retreive().then(data => {
                console.log(data)
            })
        }
    },
    mounted(){
        getTickets()
    }

}
</script>

<style scoped>  

th{
    padding-bottom: 1rem !important;
}
.bus-head{
    border-style: solid;
    border-width: 2px;
    border-radius: 20px;
    border-color: #1C5F41;
    height: 298.8px;
}
.bus-seats{
    border-style: solid;
    border-width: 2px;
    border-radius: 20px;
    width: 740px !important;
    border-color: #1C5F41;
}
.list-group-item{
  border-width: 2px !important;
  border-color: #1C5E3C;
  border-radius: 17px !important;
  width: 49px !important;
  color: #1C5E3C;
  font-size: 28px;
  padding: .1rem .1rem !important;
}
.availableSeat{
    background-color: #FFF;
    cursor: pointer;
}
.occupiedSeat{
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
}
.collapse, .collapsing{
    background-color: #FFF;
    padding: 0 !important;
    margin: 0 !important;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}
th{
    min-width: 33.3% !important;
}
.form-control, .form-control-plaintext{
    border-bottom: none !important;
    border-radius: 15px;
}
select{
    background-color:#FFF !important;
}
.colour{
    border-width: 2px !important;
    border-color: #1C5E3C;
    border-radius: 17px !important;
}
</style>