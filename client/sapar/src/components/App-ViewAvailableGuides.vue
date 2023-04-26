<template>
    <div class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">Vasya Pupkin</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> Experience: 2 years</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Based in: Almaty</h5>
                        <h5 class="my-3"><i class="bi bi-map"></i> Is involved in 4 guided tours</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <button type="button" class="btn btn-primary">{{ $t('Hire') }}</button>
                    </div>
                </div>
            </div>
            <div class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">Vasya Pupkin</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> Experience: 2 years</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Based in: Almaty</h5>
                        <h5 class="my-3"><i class="bi bi-map"></i> Is involved in 4 guided tours</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <button type="button" class="btn btn-primary">{{ $t('Hire') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
    import TourService from '@/services/TourService';

    export default {
        props: ['tourId'],
        data() {
            return {
                tour: null
            }
        },
        methods: {
            async getTour() {
                TourService.retreiveById(this.tourId)
            }
        },

        async mounted() {
            await this.getTour();
        }
        
    }
</script>

<style scoped> 


.tours{
    background-color: #FFF;
}
</style>