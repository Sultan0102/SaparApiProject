<template>
    <div class="container-fluid py-5 mt-5" v-if="availableGuides">
        <div class="container">
            <div v-for="guide in availableGuides"
            :key="guide.id"
            class="row align-items-center tours mb-1 p-3"
            >
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">{{ guide.user.firstName + ' ' + guide.user.lastName }}</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> Experience: 2 years</h5>
                        <h5 class="my-3"><i class="bi bi-star"></i> Service Rating: {{ guide.serviceRating }}</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Based in: Almaty</h5>
                        <h5 class="my-3"><i class="bi bi-map"></i> Is involved in 4 guided tours</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <router-link :to="{
                            name: 'GuideHire',
                            params: { tourId: tourId, guideId: guide.id }
                        }">
                            <button type="button" class="btn btn-primary">{{ $t('Hire') }}</button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
    import TourService from '@/services/TourService';
    import UserService from '@/services/UserService';

    export default {
        props: ['tourId'],
        data() {
            return {
                tour: null,
                availableGuides: null
            }
        },

        computed: {
            tourGuides: function() {
                return this.tour.guides;
            }
        },
        methods: {
            async getTour() {
                await TourService.retreiveById(this.tourId).then(
                    (data) => {
                        this.tour = data
                    }
                )
            },

            async getAvailableGuides() {
                await UserService.retreiveGuides().then(
                    (data) => {
                        console.log(data)
                        console.log(this.tourGuides)
                        this.availableGuides = data.filter(g => !this.tourGuides.map(tg => tg.id).includes(g.id))
                    }
                )
            }
        },

        async mounted() {
            await this.getTour();
            await this.getAvailableGuides();
            console.log(this.availableGuides)
        }
        
    }
</script>

<style scoped> 


.tours{
    background-color: #FFF;
}
</style>