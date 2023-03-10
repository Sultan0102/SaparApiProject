import Api from "./Api"

class ScheduleService{
    getSchedules(fromDate, toDate, lang_id, scheduleTypeId) {
        return Api.schedules.post(data={
            fromDate,
            toDate,
            lanuguage_id:lang_id,
            scheduleType: scheduleTypeId
        })
    }
}

export default new ScheduleService()