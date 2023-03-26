import Api from "./Api"

class ScheduleService{
    getSchedules(fromDate, toDate, lang_id, scheduleTypeId) {
        return Api.schedules.post('', {
            fromDate,
            toDate,
            language_id:lang_id,
            scheduleType: scheduleTypeId
        }).then((response)=> {
            return response.data;
        })
    }
}

export default new ScheduleService()