import Api from "./Api"

class ScheduleService{
    getSchedules(criteria) {
        return Api.schedules.post('', {
            fromDate: criteria.fromDate,
            toDate: criteria.toDate,
            language_id: criteria.language_id,
            scheduleType: criteria.scheduleTypeId,
            isActive: criteria.isActive
        }).then((response)=> {
            return response.data;
        })
    }
}

export default new ScheduleService()