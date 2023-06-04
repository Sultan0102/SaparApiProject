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
                                
                                <tr v-for="tour in tours"
                                :key="tour.id"
                                @click="editTour(tour.id)"
                                >
                                    <th>{{ getTourName(tour) }}</th>
                                    <th>{{ getTourSourceAndDestination(tour) }}</th>
                                    <th>{{ getFormattedTimeStr(tour) }}</th>
                                    <th>{{ getFormattedDateStr(tour.deletedDate) }}</th>
                                    <!-- <th>{{  }}</th> -->
                                </tr>   
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

export default{
    components: {
        Navigation
    },
    data() {
        return {
            tours: [],
            scheduleType: 2,
            
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

        getFormattedTimeStr(tour) {
            let schedule = tour.schedules[0]
            let beginTimeStr = new Date(schedule.beginDate).toLocaleTimeString('ru');
            let endTimeStr = new Date(schedule.endDate).toLocaleTimeString('ru');

            return `${beginTimeStr} - ${endTimeStr}`
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