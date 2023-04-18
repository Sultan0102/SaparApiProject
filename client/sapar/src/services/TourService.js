import Api from "./Api"

class TourService{
    createTour(tour) {
        return Api.tours.post('', {
            title: tour.title,    
            description: tour.description,    
            owner: tour.owner,    
            price: tour.price,    
            source: tour.source,    
            destination: tour.destination,    
            weekDays: tour.weekDays,    
            beginTime: tour.beginTime,    
            endTime: tour.endTime, 
            languageId: tour.languageId
        }).then((response)=> {
            return response.data;
        })
    }
}

export default new TourService()