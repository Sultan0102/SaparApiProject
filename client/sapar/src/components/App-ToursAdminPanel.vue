<template>  
    <div v-if="tours" class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9 text-center">
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col">{{ $t('Tour') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('From') }} - {{ $t('To') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Departure - Arrival Time') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Is Deleted') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <template v-for="tour in tours"
                                :key="tour.id"
                                >
                                <tr :id="'tour_'+tour.id" data-bs-toggle="collapse" :data-bs-target="'#tour_schedules_'+tour.id" >
                                    <th>{{ getTourName(tour) }}</th>
                                    <th>{{ getTourSourceAndDestination(tour) }}</th>
                                    <th>{{ getFormattedTourTimeStr(tour) }}</th>
                                    <th>{{ getFormattedDateStr(tour.deletedDate) }}</th>
                                </tr>
                                <tr v-for="schedule in tour.schedules"
                                :id="'tour_schedules_'+tour.id" 
                                class="collapse">
                                    <td>{{ schedule.scheduleNumber }}</td>
                                    <td>{{ getFormattedDateStr(schedule.beginDate) }}</td>
                                    <td>{{ `${getFormattedTimeStr(schedule.beginDate)} - ${getFormattedTimeStr(schedule.endDate)}` }}</td>
                                    <th>{{ getFormattedDateStr(schedule.deletedDate) }}</th>
                                    <th>
                                        <Toggle v-model="schedule.isActive"
                                        offLabel="Not Active"
                                        onLabel="Active"
                                        @click="changeActivity(tour, schedule)"
                                        />
                                    </th>
                                </tr>
                                </template>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>



<script>
import Navigation from "@/components/App-NavigationAdminPanel.vue";
import ScheduleService from "@/services/ScheduleService";
import TourService from "@/services/TourService";
import Toggle from '@vueform/toggle'


export default{
    components: {
        Navigation,
        Toggle
    },
    data() {
        return {
            tours: [],
            scheduleType: 2,
            switchVal: true
            
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

        getTourName(tour) {
            return tour.titleNameCode.defaultValue;
        },

        getTourSourceAndDestination(tour) {
            let schedule = tour.schedules[0]
            return `${schedule.route.sourceName} - ${schedule.route.destinationName}`
        },

        getFormattedDateStr(dateStr) {
            if (dateStr == null) return ' - '
            let date = new Date(dateStr);

            return date.toLocaleDateString('ru')
        },

        getFormattedTourTimeStr(tour) {
            let schedule = tour.schedules[0]
            let beginTimeStr = new Date(schedule.beginDate).toLocaleTimeString('ru');
            let endTimeStr = new Date(schedule.endDate).toLocaleTimeString('ru');

            return `${beginTimeStr} - ${endTimeStr}`
        },
        getFormattedTimeStr(dateStr) {
            if (dateStr == null) return ' - '
            let date = new Date(dateStr);

            return date.toLocaleTimeString('ru')
        },

        getIsActiveStr(isActive) {
            if(isActive) return "Is Enabled"

            return "Is Disabled"
        },

        async changeActivity(tour, schedule) {
            const criteria = {
                'tourId': tour.id,
                'scheduleId': schedule.id,
                'isActive': schedule.isActive
            }
            console.log(criteria);
            await TourService.updateTourScheduleActivity(criteria).then(
                (data)=> {
                    this.$notify({
                        type: 'success',
                        title: 'Update Tour Schedule',
                        text: 'Successfully updated tour schedule activity'
                    })
                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: 'Update Tour Schedule',
                        text: 'Error updating tour schedule activity'
                    })
                }
            )
        },

        editTour(tourId) {
            // this.$router.push({
            //     name: 'NewRouteEdit',
            //     params: { scheduleId: scheduleId }
            // })
        },
        async getTours() {
            //
            await TourService.retreiveWithDepth(1).then(
                (data)=> {
                    this.tours = data
                }
            )
        },
    },
    async mounted() {
        await this.getTours()
        console.log(this.tours);
    }
}
</script>

<style src="@vueform/toggle/themes/default.css"></style>

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