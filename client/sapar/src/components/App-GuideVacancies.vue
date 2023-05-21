<template>
    <div class="container-fluid py-5 mt-5">
        <div v-if="tours" class="container">
            <div v-for="tour in tours"
            :key="tour.id" 
            class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">{{ tour.schedules[0].route.sourceName }} <i class="bi bi-arrow-right"></i> {{ tour.schedules[0].route.destinationName}}</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> 8 hour in general</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Sayran, Almaty</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <h4>{{ $t('Available Guides') }}:</h4>
                        <h2>
                            <i v-for="guide in tour.guides"
                            class="bi bi-person-circle me-2">
                            </i>
                        </h2>
                        <router-link :to="{
                            name: 'GuideApply',
                            params: { tourId: tour.id }
                        }">
                            <button type="button" class="btn btn-primary text-center mx-auto">Apply</button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import TokenService from '@/services/TokenService';
import TourService from '@/services/TourService';


export default {
    data() {
        return {
            tours: null
        }
    },
    computed: {
        
    },
    methods: {
        async getTours() {
            const userId = TokenService.getUser().id;
            await TourService.retreiveNonDeleted().then(
                (data)=> {
                    // Take tours that have no current guide on them
                    this.tours = data.filter(tour => tour.guides.filter(g => g.user.id == userId).length == 0);   
                },
                (error) => {
                    console.log(error)
                }
            )
            console.log(this.tours)
            
        }
    },
    async mounted() {
        await this.getTours();
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
</style>