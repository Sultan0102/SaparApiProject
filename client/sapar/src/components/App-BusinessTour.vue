<template>
    <div class="row align-items-center tours mb-1 p-3">
        <div class="col-md-3">
            <img src="../assets/Experience.png" class="img-fluid">
        </div>
        <div class="col-md-5">
            <div class="text-md-start text-center">
                <h2 class="my-3">{{ tour.schedules[0].route.sourceName }} <i class="bi bi-arrow-right"></i> {{ tour.schedules[0].route.destinationName}} </h2>
                <h5 class="my-3"><i class="bi bi-clock"></i> 8 hour in general</h5>
                <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Sayran, Almaty</h5>
            </div>
        </div>
        <div class="col-md-4">
            <div class="mt-4 mt-md-0 text-center">
                <h4>{{ $t('Available Guides') }}:</h4>
                <h2>
                    <i v-for="guide in tour.guides"
                    :key="guide.id"
                    class="bi bi-person-circle me-2"
                    >
                    </i>
                </h2>
                <button type="button" class="btn btn-primary mb-3" data-bs-toggle="collapse" :data-bs-target="`#${tourSelectorId}`">{{ $t('Modify') }}</button>
            </div>
        </div>

        <div :id="tourSelectorId" class="collapse tours">
            <div class="row">
                <div class="col-12 d-flex justify-content-center">
                    <button type="button" class="btn btn-primary m-3" data-bs-toggle="collapse">{{ $t('Hire') }}</button>
                </div>
            </div>
            <div class="row my-5 ">
                <div v-for="guide in tour.guides"
                :key="guide.id" 
                class="col-5 row mb-5 mb-md-3">
                    <div class="col-lg-6 my-auto">
                        <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>{{guide.user.firstName}} {{ guide.user.lastName[0] }}.</h3>
                    </div>
                    <div class="col-lg-4 my-auto">
                        <button type="button" class="btn btn-primary text-center me-auto">{{ $t('Fire') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    props: ['tour'],
    data() {
        return {
            
        }
    },

    computed: {
        tourSelectorId: function() {
            return `tour_${this.tour.id}`
        }
    },

    methods: {
        
    },
    mounted() {
        console.log(this.tour)
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