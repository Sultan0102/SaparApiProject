import Api from "./Api"

class TicketService{
    retreive(id) {
        return Api.tickets.get().then(function(response) {
            return response.data;
        })
    }
}

export default new TicketService()