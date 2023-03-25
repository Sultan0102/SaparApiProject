import Api from "./Api"

class TicketPersonService{
    create(person) {
        return Api.ticketPersons.post('', {
            firstName: person.firstName,  
            lastName: person.lastName,  
            secondName: person.secondName,  
            passportNumber: person.passportNumber,  
            passportNumberType: person.passportNumberType,  
            ticketId: person.ticketId,  
        })
    }
    
    getCachedTicketPerson(userId) {
        return Api.cachedTicketPersons.get(`?userId=${userId}`).then((response)=> {
            return response.data;
        })
    }

    saveCachedTicketPerson(person) {
        return Api.cachedTicketPersons.post('', {
            firstName: person.firstName,  
            lastName: person.lastName,  
            secondName: person.secondName,  
            passportNumber: person.passportNumber,  
            passportNumberType: person.passportNumberType,  
            ticketId: person.ticketId,
            user: person.user  
        })
    }
}

export default new TicketPersonService()