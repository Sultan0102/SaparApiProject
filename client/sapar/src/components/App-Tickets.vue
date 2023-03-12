<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="col-xl-6 mx-auto mb-3">
            <input type="search" class="form-control" placeholder="Search here" aria-label="Search">
        </div>
        <div class="container table-responsive">
            <table class="table table-hover text-center">
                <thead>
                    <tr>
                        <th scope="col">{{ $t('     Route    ') }}</th>
                        <th scope="col">{{ $t('   From - To  ') }}</th>
                        <th scope="col">{{ $t('Departure - Arrival Time') }}</th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="schedule in schedules">
                        <tr data-bs-toggle="collapse" :data-bs-target="'#'+schedule.scheduleNumber">
                            <th scope="row"><span id="schedule-number">{{ schedule.scheduleNumber }}</span></th>
                            <td><span id="route-source-dest">{{ concatenatedSourceAndDestination(schedule) }}</span></td>
                            <td><span id="begin-end-date">{{ concatenatedBeginDateAndEndDate(schedule) }}</span></td>
                        </tr> 
                        <AppBus :schedule="schedule"/>

                    </template>
                                       
                </tbody>
            </table>
        </div>
    </div>

</template>

<script>
import TicketService from "@/services/TicketService"
import AppBus from "@/components/App-Bus.vue";
import ScheduleService from "@/services/ScheduleService";


export default{
    name: "Tickets",
    components: {
        AppBus
    },
    data() {
        return {
            schedules: null,
            filters: {
                beginDate: new Date(2023,0, 16),
                endDate: new Date(2023, 1, 11)
            },
            locales: {
                'en': 3,
                'ru': 1,
                'kz': 2
            }
        };
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
      
      formattedBeginDateString: function() {
        let beginDate = this.filters.beginDate;
        return beginDate.toISOString().split('T')[0]
      },
      formattedEndDateString: function() {
        let endDate = this.filters.endDate;
        return endDate.toISOString().split('T')[0]
      } 
    },
    methods: {
        

        getSchedules() {
            let langId = this.currentLanguageId;
            console.log(`Lang ID: ${langId}`) 
            console.log(`Dates`)
            console.log(this.formattedBeginDateString)
            console.log(this.formattedEndDateString)

            ScheduleService.getSchedules(this.formattedBeginDateString, this.formattedEndDateString, langId, 1).then((schedules)=> {
                this.schedules = schedules;
            },
            (error)=> {
                 
            })
        },

        concatenatedSourceAndDestination: function (schedule) {
            return schedule.route.sourceName + ' - ' + schedule.route.destinationName;
        },
        concatenatedBeginDateAndEndDate: function(schedule) {
            return schedule.beginDate.split('T')[1] + ' ' + schedule.endDate.split('T')[1]
      },
    },
    mounted() {
        this.getSchedules();
    },
    components: { AppBus }
}
</script>

<style scoped>  
 th{
    padding-bottom: 1rem !important;
    min-width: 33.3% !important;
}

</style>