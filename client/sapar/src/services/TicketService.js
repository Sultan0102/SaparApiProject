import Api from "./Api"

class TicketService{
    retreive(id) {
        return Api.tickets.get().then(function(response) {
            return response.data;
        })
    }
    
    getUserTickets(userId) {
        return Api.tickets.get(`?userId=${userID}/`).then((response)=> {
            return response.data
        });
    }

    getPassportTypes() {
        return Api.passportTypes.get().then(
            (response)=> {
                return response.data
            }
        )
    }
}

export default new TicketService()