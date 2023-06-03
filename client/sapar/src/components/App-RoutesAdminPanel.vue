<template>  
    <div v-if="schedules" class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9 text-center">
                    <div class="mx-auto mb-3 ms-5 mt-4">
                        <div class="input-group">
                            <input type="search" class="form-control" :placeholder="$t('By schedule number:')" aria-label="Search">
                            <button class="btn search" type="button"><i class="bi bi-search"></i></button>
                        </div>
                    </div>
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col">{{ $t('Schedule') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('From') }} - {{ $t('To') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Departure - Arrival Time') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                
                                <tr v-for="schedule in schedules"
                                :key="schedule.id"
                                @click="editRoute(schedule.id)"
                                >
                                    <th>{{ schedule.scheduleNumber }}</th>
                                    <th>{{ `${schedule.route.sourceName} - ${schedule.route.destinationName}` }}</th>
                                    <th>{{ formattedScheduleDate(schedule) }}</th>
                                </tr>   
                            </tbody>
                        </table>
                    </div>
                    
                    <router-link class="nav-link" :to="{name: 'NewRoute'}"><button type="submit" class="btn btn-primary mt-5">{{ $t('New') }}</button></router-link>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import Navigation from "@/components/App-NavigationAdminPanel.vue";
import ScheduleService from "@/services/ScheduleService";

export default{
    components: {
        Navigation
    },
    data() {
        return {
            schedules: [],
            scheduleType: 1
        }
    },
    computed: {
        currentLanguageId: function() {
            let currentLocale = this.$i18n.locale;
            let langId = null;
            switch(currentLocale) {
                case 'en':
                    langId = 3;
                    break;
                case 'kz':
                    langId = 2;
                    break;
                case 'ru':
                    langId = 1;
                    break;
                default:
                    langId = 1;
                    break;
            }
            return langId;
        },
    },
    methods: {
        formattedDateString(date) {

            return date != null
                ? date.toISOString().split('T')[0]
                : null;
        }, 
        getTimeZonedDate(dateStr) {
            let timeZonedDateStr = new Date(dateStr).toLocaleString('ru', {timeZone: 'Asia/Almaty'})
            
            return new Date(timeZonedDateStr);
        },
        formattedScheduleDate(schedule) {
            let timezonedBeginDate = this.getTimeZonedDate(schedule.beginDate)
            let timezonedEndDate = this.getTimeZonedDate(schedule.endDate)
            
            return `${timezonedBeginDate.toLocaleTimeString('ru', { hour: '2-digit', minute:'2-digit'})} - ${timezonedEndDate.toLocaleTimeString('ru', { hour: '2-digit', minute:'2-digit'})}`
        },
        editRoute(scheduleId) {
            this.$router.push({
                name: 'NewRouteEdit',
                params: { scheduleId: scheduleId }
            })
        },
        async getSchedules() {
            let langId = this.currentLanguageId;

            const criteria = {
                language_id: langId,
                scheduleTypeId: this.scheduleType,
                fromDate: this.formattedDateString(new Date(2023, 1, 1)),
                toDate: this.formattedDateString(new Date(2023, 11, 30))
            }
            await ScheduleService.getSchedules(criteria).then(
                (data)=> {
                    this.schedules = data
                }
            )
        }
    },
    async mounted() {
        await this.getSchedules()
        console.log(this.schedules);
    }
}
</script>

<style scoped>  
*{
	color: #1C5E3C;
}
th{
    padding-bottom: 1rem !important;
    min-width: 33.3% !important;
}
.filter-icon{
    width: 15px;
}
.input-group{
    max-width: 1300px;
}
.search{
    border-bottom-right-radius: 15px !important;
	border-top-right-radius: 15px !important;
    background-color: #FFF !important;
}
.form-control, .form-control-plaintext{
    border-bottom: none !important;
    border-radius: 15px;
}
</style>