<template>
    <div class="container-fluid py-5">
        <div class="container">
            <table class="table table-hover text-center">
                <thead>
                    <tr>
                    <th scope="col">{{ $t('Route') }}</th>
                    <th scope="col">{{ $t('From') }}</th>
                    <th scope="col">{{ $t('To') }}</th>
                    <th scope="col">{{ $t('Departure Time') }}</th>
                    <th scope="col">{{ $t('Arrival Time') }}</th>
                    </tr>
                </thead>
                <tbody>

                        <tr type="button" data-bs-toggle="collapse" data-bs-target="#bus1">
                            <th scope="row">AB4958</th>
                            <td>Almaty</td>
                            <td>Taraz</td>
                            <td>10:40pm</td>
                            <td>05:30pm</td>
                            
                        </tr>   
                        <td colspan="5" class="collapse" id="bus1">
                            <div class="collapse" id="bus1">
                                    <ul class="list-group list-group-horizontal-sm">
                                        <li v-for="ticket in tickets" class="list-group-item me-3 availableSeat">{{ ticket.seatNumber }}</li>
                                    </ul>
                                    <ul class="list-group list-group-horizontal-sm">
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                        <li class="list-group-item">1</li>
                                    </ul>
                                    
                            </div>
                        </td>


                </tbody>
            </table>
        </div>
    </div>
    
</template>

<script>
export default{
    data(){
        return{
            tickets:[
            { id: 1, seatNumber: 1, ticketStatus: 0},
            { id: 2, seatNumber: 2, ticketStatus: 0},
            { id: 3, seatNumber: 3, ticketStatus: 0},
            { id: 4, seatNumber: 4, ticketStatus: 0},
            { id: 5, seatNumber: 5, ticketStatus: 0},
            { id: 6, seatNumber: 6, ticketStatus: 0},
            { id: 7, seatNumber: 7, ticketStatus: 0},
            { id: 8, seatNumber: 8, ticketStatus: 0},
            { id: 9, seatNumber: 9, ticketStatus: 0},
            { id: 10, seatNumber: 10, ticketStatus: 0},
            { id: 11, seatNumber: 11, ticketStatus: 0},
            { id: 12, seatNumber: 13, ticketStatus: 0},
            { id: 13, seatNumber: 13, ticketStatus: 0},
            ]
        }
    },
    methods:{
        currentStatusColor(n){
            switch(this.tickets.ticketStatus){
                    case 0:
                        return availableSeat
                    case 1:
                        return occupiedSeat
                    case 2:
                        return bookedSeat

            }
        }
    }

}
</script>

<style scoped>  
*{
    color: #1C5E3C;
}
th{
    padding-bottom: 1rem !important;
}
collapse{
    padding: none !important;
}
.list-group-item{
  border-width: 2px !important;
  border-color: #1C5E3C;
  border-radius: 10px !important;
  max-width:100%;
}
.availableSeat{

}
.occupiedSeat{

}
.bookedSeat{

}
</style>