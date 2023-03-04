<template>
<tr data-bs-toggle="collapse" data-bs-target="#bus3">
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
</td>
</template>

<script>
export default {
    data() {
        return {
            tickets: [[{ "id": 1, "seatNumber": 1, "ticketStatus": 1 }, { "id": 2, "seatNumber": 2, "ticketStatus": 2 }, { "id": 3, "seatNumber": null, "ticketStatus": 0 }, { "id": 4, "seatNumber": 3, "ticketStatus": 2 }, { "id": 5, "seatNumber": 4, "ticketStatus": 1 }], [{ "id": 6, "seatNumber": 5, "ticketStatus": 1 }, { "id": 7, "seatNumber": 6, "ticketStatus": 2 }, { "id": 8, "seatNumber": null, "ticketStatus": 0 }, { "id": 9, "seatNumber": 7, "ticketStatus": 2 }, { "id": 10, "seatNumber": 8, "ticketStatus": 1 }], [{ "id": 11, "seatNumber": 9, "ticketStatus": 2 }, { "id": 12, "seatNumber": 10, "ticketStatus": 1 }, { "id": 13, "seatNumber": null, "ticketStatus": 0 }, { "id": 14, "seatNumber": 11, "ticketStatus": 1 }, { "id": 15, "seatNumber": 12, "ticketStatus": 2 }], [{ "id": 16, "seatNumber": 13, "ticketStatus": 1 }, { "id": 17, "seatNumber": 14, "ticketStatus": 1 }, { "id": 18, "seatNumber": null, "ticketStatus": 0 }, { "id": 19, "seatNumber": null, "ticketStatus": 0 }, { "id": 20, "seatNumber": null, "ticketStatus": 0 }], [{ "id": 21, "seatNumber": 17, "ticketStatus": 1 }, { "id": 22, "seatNumber": 18, "ticketStatus": 2 }, { "id": 23, "seatNumber": null, "ticketStatus": 0 }, { "id": 24, "seatNumber": 19, "ticketStatus": 1 }, { "id": 25, "seatNumber": 20, "ticketStatus": 1 }], [{ "id": 26, "seatNumber": 21, "ticketStatus": 1 }, { "id": 27, "seatNumber": 22, "ticketStatus": 1 }, { "id": 28, "seatNumber": null, "ticketStatus": 0 }, { "id": 29, "seatNumber": 23, "ticketStatus": 1 }, { "id": 30, "seatNumber": 24, "ticketStatus": 1 }], [{ "id": 31, "seatNumber": 25, "ticketStatus": 1 }, { "id": 32, "seatNumber": 26, "ticketStatus": 1 }, { "id": 33, "seatNumber": null, "ticketStatus": 0 }, { "id": 34, "seatNumber": 27, "ticketStatus": 1 }, { "id": 35, "seatNumber": 28, "ticketStatus": 1 }], [{ "id": 36, "seatNumber": 29, "ticketStatus": 1 }, { "id": 37, "seatNumber": 30, "ticketStatus": 1 }, { "id": 38, "seatNumber": null, "ticketStatus": 0 }, { "id": 39, "seatNumber": null, "ticketStatus": 0 }, { "id": 40, "seatNumber": null, "ticketStatus": 0 }], [{ "id": 41, "seatNumber": 33, "ticketStatus": 1 }, { "id": 42, "seatNumber": 34, "ticketStatus": 2 }, { "id": 43, "seatNumber": null, "ticketStatus": 0 }, { "id": 44, "seatNumber": 35, "ticketStatus": 2 }, { "id": 45, "seatNumber": 36, "ticketStatus": 1 }], [{ "id": 46, "seatNumber": 37, "ticketStatus": 1 }, { "id": 47, "seatNumber": 38, "ticketStatus": 2 }, { "id": 48, "seatNumber": null, "ticketStatus": 0 }, { "id": 49, "seatNumber": 39, "ticketStatus": 2 }, { "id": 50, "seatNumber": 40, "ticketStatus": 1 }], [{ "id": 51, "seatNumber": 41, "ticketStatus": 2 }, { "id": 52, "seatNumber": 42, "ticketStatus": 1 }, { "id": 53, "seatNumber": null, "ticketStatus": 0 }, { "id": 54, "seatNumber": 43, "ticketStatus": 1 }, { "id": 55, "seatNumber": 44, "ticketStatus": 2 }]],
        }
    },
    methods: {
        currentStatusColor(n) {
            switch (n) {
                case 0:
                    return "empty-space";
                case 1:
                    return "availableSeat";
                case 2:
                    return "occupiedSeat";
                case 3:
                    return "bookedSeat";
            }
        },
        currentStatussColo(n) {
            switch(n) {
                case 0: 
                    return"empty-space";
                case 1: 
                    return "acailableSeat";
                case 2: 
                    return " bookedSeat";

            }
        },
        occupySeat(ticket) {
            if (ticket.ticketStatus == 1 && this.ticketsSum < 5) {
                ticket.ticketStatus = 3;
                this.ticketsSum++;
            }
            else if (ticket.ticketStatus == 3) {
                ticket.ticketStatus = 1;
                this.ticketsSum--;
            }
            else {
                console.log(ticket.ticketStatus);
            }
            console.log(this.ticketsSum);
            console.log(this.tickets.filter(t => t.ticketStatus == 3));
        },
    }

}

</script>



<style scoped>  
th{
    padding-bottom: 1rem !important;
    min-width: 33.3% !important;
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
.form-control, .form-control-plaintext{
    border-bottom: none !important;
    border-radius: 15px;
}
select{
    background-color:#FFF !important;
}
.colour{
    max-width: 150px;
    border-width: 2px !important;
    border-color: #1C5E3C !important;
    border-radius: 17px !important;
    border-style: solid !important;
    cursor: default;
}

</style>