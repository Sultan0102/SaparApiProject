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

            <div class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">Almaty <i class="bi bi-arrow-right"></i> Kolsai</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> 8 hour in general</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Sayran, Almaty</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <h4>{{ $t('Available Guides') }}:</h4>
                        <h2><i class="bi bi-person-circle me-2"></i><i class="bi bi-person-circle me-2"></i><i class="bi bi-person-circle me-2"></i><i class="bi bi-person-circle me-2"></i><i class="bi bi-person-circle me-2"></i></h2>
                        <button type="button" class="btn btn-primary mb-3" data-bs-toggle="collapse" data-bs-target="#tour">{{ $t('Modify') }}</button>
                    </div>
                </div>
                <div class="collapse tours" id="tour">
                    <div class="row my-5 ">
                        <div class="col-5 row mb-5 mb-md-3">
                            <div class="col-lg-6 my-auto">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Elena K.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center me-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                        <div class="col-5 row mb-5 mb-md-3 mx-auto ps-5">
                            <div class="col-lg-6">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Elena K.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                        <div class="col-5 row mb-5 mb-md-3">
                            <div class="col-lg-6">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Yuri L.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                        <div class="col-5 row mb-5 mb-md-3 mx-auto ps-5">
                            <div class="col-lg-6">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Yuri L.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                        <div class="col-5 row mb-5 mb-md-3">
                            <div class="col-lg-6">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Klavdiya M.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">Almaty <i class="bi bi-arrow-right"></i> Kolsai</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> 8 hour in general</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Sayran, Almaty</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <h4>{{ $t('Available Guides') }}:</h4>
                        <h2><i class="bi bi-person-circle me-2"></i>+</h2>
                        <button type="button" class="btn btn-primary text-center mx-auto mb-3" data-bs-toggle="collapse" data-bs-target="#tour2">{{ $t('Modify') }}</button>
                    </div>
                </div>
                <div class="collapse tours" id="tour2">
                    <div class="row my-5">
                        <div class="col-5 row mb-5 mb-md-3">
                            <div class="col-lg-6 my-auto">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Elena K.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-5">
                    <div class="text-md-start text-center">
                        <h2 class="my-3">Almaty <i class="bi bi-arrow-right"></i> Kolsai</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> 8 hour in general</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Sayran, Almaty</h5>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mt-4 mt-md-0 text-center">
                        <h4>{{ $t('Available Guides') }}:</h4>
                        <h2><i class="bi bi-person-circle me-2"></i><i class="bi bi-person-circle me-2"></i></h2>
                        <button type="button" class="btn btn-primary text-center mx-auto mb-3" data-bs-toggle="collapse" data-bs-target="#tour3">{{ $t('Modify') }}</button>
                    </div>
                </div>
                <div class="collapse tours" id="tour3">
                    <div class="row my-5">
                        <div class="col-5 row mb-5 mb-md-3">
                            <div class="col-lg-6 my-auto">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Elena K.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                        <div class="col-5 row mb-5 mb-md-3 mx-auto ps-5">
                            <div class="col-lg-6">
                                <h3 class="my-auto"><i class="bi bi-person-circle person align-middle me-3"></i>Elena K.</h3>
                            </div>
                            <div class="col-lg-4 my-auto">
                                <button type="button" class="btn btn-primary text-center mx-auto">{{ $t('Fire') }}</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 
        </div>
    </div>
    
</template>

<script>

export default {
    data() {

    },

    methods: {
        
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