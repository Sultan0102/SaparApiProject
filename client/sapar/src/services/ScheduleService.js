import Api from "./Api"

class ScheduleService{
    getSchedules(criteria) {
        return Api.schedules.post('', {
            source: criteria.source,
            destination: criteria.destination,
            fromDate: criteria.fromDate,
            toDate: criteria.toDate,
            language_id: criteria.language_id,
            scheduleType: criteria.scheduleTypeId,
            isActive: criteria.isActive
        }).then((response)=> {
            return response.data;
        })
    }

    retreive(scheduleId) {
        return Api.schedules.get(`${scheduleId}/`).then(
            (response) => {
                return response.data;
            }
        )
    }

    createIntercityBusSchedule(criteria) {
        return Api.schedules.post('intercity/', criteria).then(
            (response)=> {
                return response.data
            }
        )
    }

    updateIntercitySchedule(criteria) {
        return Api.schedules.post('intercity/update/', criteria).then(
            (response)=> {
                return response.data; 
            }
        )
    }
}

export default new ScheduleService()