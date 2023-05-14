<template>
    <div class="row" v-if="tour">
        <div class="col-10">{{ applicationStatus }} {{ applicationTypeHeader }} Application <br/> {{ applicationTypeHeader }} {{applicationSubjectInitials}} from/for Tour {{ scheduleNumber }}</div>
        
        <div v-if="application.status == 1" class="spinner-border col-2 mx-auto my-auto" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <div v-else-if="application.status == 2" class="col-2 text-center my-auto">
            <i class="bi bi-check-circle-fill"></i>
        </div>
    </div>

</template>


<script>
import TourService from '@/services/TourService';
import TokenService from '@/services/TokenService';


export default {
    props: ['application'],
    data() {
        return {
            tour: null
        }
    },
    computed: {
        scheduleNumber: function() {
            const schedules = this.tour.schedules
            .filter(s => new Date(s.beginDate).getDate() == new Date(this.application.applicationData.effectiveFrom).getDate());

            if (schedules.length == 0) 
                return ""
            
            return schedules[0].scheduleNumber
        },
        
        applicationTypeHeader: function() {
            let typeHeaderText = ""
            switch(this.application.type) {
                case 1: typeHeaderText = "Hiring"
                break;
                case 2: typeHeaderText = "Firing"
                break;
            }
            return typeHeaderText
        },

        applicationStatus: function() {
            let statusText = ""
            switch(this.application.type) {
                case 1: statusText = "Active" //Pending
                break;
                case 2: statusText = "Approved"
                break;
                case 2: statusText = "Rejected"
                break;
            }

            return statusText
        },

        applicationSubjectInitials: function() {
            const user = TokenService.getUser();
            if(user.role == 4 || user.role == 3) { // if opened by business person
                return this.application.applicationData.firstName + ' ' + this.application.applicationData.lastName.substring(0,1) + '.';
            }

            return ""
        }

    },
    methods: {
        async getTour() {
            await TourService.retreiveById(this.application.applicationData.tour).then(
                (data) => {
                    this.tour = data
                }
            )
        }
    },
    async mounted() {
        await this.getTour();
    }
}
</script>

<style scoped>

.list-group-item{
    border: none !important;
    border-bottom: 1px solid #ECECEC !important;
}
.bi-check-circle-fill{
    font-size: 2rem !important;
}
</style>
