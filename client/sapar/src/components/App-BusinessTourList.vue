<template>
    <div class="container-fluid py-5 mt-5">

        <div class="container">
            <div class="row mb-1 p-3">
                <div class="col-md-12 text-center">
                    <router-link to="/new-tour">
                        <button type="button" class="btn btn-primary mb-3" @click="">{{ $t('New Tour') }}</button>
                    </router-link>
                </div>
            </div>

            <AppBusinessTour v-for="tour in tours"
            :key="id" 
            :tour="tour"
            />
        </div>
    </div>
    
</template>

<script>
import AppBusinessTour from '@/components/App-BusinessTour.vue';
import TourService from '@/services/TourService';


export default {
    components: {
        AppBusinessTour
    },
    data() {
        return {
            tours: []
        }
    },

    methods: {
        async getTours() {
            let tours = null
            await TourService.retreiveNonDeleted().then(
                (data)=> {
                    tours = data
                },
                (error)=> {

                }
            )

            this.tours = tours.filter(t => this.hasRelevantSchedules(t))
            
        },

        hasRelevantSchedules(tour) {
            for(let i in tour.schedules) {
                let beginDate = new Date(tour.schedules[i].beginDate)
                if (beginDate > new Date()) 
                    return true;
            }
            return false
        }
    },
    async mounted() {
        await this.getTours()
    }
}
</script>

<style scoped> 
.tours{
    background-color: #FFF;
}
.btn-primary{
	min-width: 150px;
    font-size: 24px;
}
.person{
    font-size: 48px;
}
</style>