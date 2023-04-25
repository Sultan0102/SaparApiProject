<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="col-xxl-8 col-10 mx-auto mb-3">
            <div class="input-group mx-auto">
                <input v-model="filters.source" type="search" class="form-control" :placeholder="$t('From')" aria-label="Search">
                <input v-model="filters.destination" type="search" class="form-control" :placeholder="$t('To')"  aria-label="Search">
                <div class="form-control">
                    <VueDatePicker 
                    v-model="filters.dateRange" 
                    model-auto 
                    range 
                    :min-date="new Date()"
                    position="right"
                    :format="formatDateRange"
                    hide-input-icon />
                </div>
                <button class="btn search" type="button" @click="filterSchedules"><i class="bi bi-search"></i></button>
            </div>
        </div>
        <div class="container table-responsive">
            <table class="table table-hover text-center">
                <thead>
                    <tr>
                        <th scope="col">{{ $t('Route') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                        <th scope="col">{{ $t('From') }} - {{ $t('To') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                        <th scope="col">{{ $t('Departure - Arrival Time') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
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
    props: ['scheduleType'],
    name: "Tickets",
    components: {
        AppBus
    },
    data() {
        return {
            schedules: null,
            filters: {
                source: null,
                destination: null,
                beginDate: new Date(),
                endDate: null,
                dateRange: new Date()
            },
            locales: {
                'en': 3,
                'ru': 1,
                'kz': 2
            },
            scheduleType: 1
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

        return endDate != null
               ? endDate.toISOString().split('T')[0]
               : null;
      } 
    },
    methods: {
        
        formatDateRange(dates) {
            let dateStrings = []
            dates.forEach((date) => {

                if(date) {
                    const day = date.getDate();
                    const month = date.getMonth();
                    const year = date.getFullYear();
    
                    dateStrings.push(`${day}.${month}.${year}`)
                }
            })
            
            
            return dateStrings.join(' - ');
        },

        getSchedules() {
            let langId = this.currentLanguageId;

            const criteria = {
                source: this.source,
                destination: this.destination,
                fromDate: this.formattedBeginDateString,
                toDate: this.formattedEndDateString,
                language_id: langId,
                scheduleTypeId: this.scheduleType,
                isActive: true
            }

            ScheduleService.getSchedules(criteria).then((schedules)=> {
                this.schedules = schedules;
            },
            (error)=> {
                 
            })
        },

        filterSchedules() {
            if(this.filters.dateRange == null) {
                this.filters.beginDate = new Date();
                this.filters.endDate = null
            } else {
                if(Array.isArray(this.filters.dateRange)) {
                    this.filters.beginDate = this.filters.dateRange[0]
                    this.filters.endDate = this.filters.dateRange[1]
                } else {
                    this.filters.beginDate = this.filters.dateRange;
                    this.filters.endDate = null;
                }
            }

            console.log(this.filters)
            this.getSchedules()
        },

        concatenatedSourceAndDestination: function (schedule) {
            return schedule.route.sourceName + ' - ' + schedule.route.destinationName;
        },
        concatenatedBeginDateAndEndDate: function(schedule) {
            return schedule.beginDate.split('T')[1].substring(0, 8) + ' - ' + schedule.endDate.split('T')[1].substring(0, 8)
      },
    },
    mounted() {
        this.getSchedules();
    },
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
.form-control, .form-control-plaintext{
    border-bottom: none !important;
    border-radius: 15px;
    max-width: 40% !important;
}

.collapse, .collapsing{
    background-color: #FFF;
    padding: 0 !important;
    margin: 0 !important;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}
.search{
    border-bottom-right-radius: 15px !important;
	border-top-right-radius: 15px !important;
    background-color: #FFF !important;
}
.input-group{
    max-width: 1300px;
}
.filter-icon{
    width: 15px;
}
</style>