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

    retreive() {
        return Api.tours.get('').then(
            (response)=> {
                return response.data
            }
        )
    }

    retreiveNonDeleted() {
        return Api.tours.get('', { params:{'non_deleted': 'true'} }).then(
            (response)=> {
                return response.data
            }
        )
    }

    retreiveById(tourId) {
        return Api.tours.get(`${tourId}/`).then(
            (response)=> {
                return response.data
            }
        )
    }

    retreiveByScheduleId(scheduleId, langId) {
        return Api.tours.post('schedule/', {
            scheduleId,
            languageId: langId
        }).then(
            (response)=> {
                return response.data;
            }
        )
    }
}

export default new TourService()