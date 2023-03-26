<template>
    <div class="banner-home position-relative container-fluid">
        <div class="container">
            <div class="position-absolute bottom-0 text-center mb-5 ">
                <h1 class="white my-3">{{ $t('We connect people to their dreams') }}</h1>
                <hr class="border-top" v-if="!isLoggedIn">
                <h1 class="white my-3 mb-5" v-if="!isLoggedIn">{{ $t('Join us as') }}</h1>
                <router-link to="/login" v-if="!isLoggedIn"><button type="button" class="btn btn-secondary px-3  py-1">{{ $t('A guide') }}</button></router-link>
                <router-link to="/login" v-if="!isLoggedIn"><button type="button" class="btn btn-secondary px-3 py-1 ms-5">{{ $t('A business') }}</button></router-link>
                <router-link to="/login" v-if="!isLoggedIn"><button type="button" class="btn btn-secondary btn-green px-3 py-1 ms-5">{{ $t('A customer') }}</button></router-link>
            </div>
        </div>
    </div>
<div class="container-fluid my-5">
    <div class="container">
        <h1 class="mb-5 text-center">{{ $t('90% of people using Sapar report higher satisfaction level from traveling activities') }}</h1>
        <div class="row align-items-center mb-5">
            <div class="col-md-6 text-center">
                <img src="../assets/Buy-tickets.svg" class="w-50">
            </div>
            <div class="col-md-6 text-center">
                <h3 class="text-center">{{ $t('Buy tickets to your favorite destinations within seconds!') }}</h3>
            </div>

        </div>
        <div class="row align-items-center mb-5 swap-container">
            <div class="col-md-6 text-center">
                <h3 class="text-center">{{ $t('If you are a guide, we suggest extensive collaborative tools') }}</h3>
            </div>
            <div class="col-md-6 text-center">
                <img src="../assets/If-you-are-guide.svg" class="w-50">
            </div>
        </div>
        <div class="row align-items-center mb-5">
            <div class="col-md-6 text-center">
                <img src="../assets/Buy-tickets.svg" class="w-50">
            </div>
            <div class="col-md-6 text-center">
                <h3 class="my-auto text-center">{{ $t('If you are a local tourism-based business, we offer you beneficial opportunities') }}</h3>
            </div>

        </div>
        <div id="carouselExampleDark" class="carousel carousel-dark slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
            </div>
            <h1 class="text-center pt-3">{{ $t('Trending Tours') }}</h1>
            <div class="carousel-inner pb-5">
                <div class="carousel-item active" data-bs-interval="10000">
                    <div class="row ms-3 me-3 border-top">
                        <div class="col-md-6 text-center">
                            <img src="../assets/Kolsai-Lakes.jpg" class="my-3 img-fluid">
                        </div>
                        <div class="col-md-6 my-auto ps-5">
                            <h1 class="mb-3">Almaty Kolsai Lake</h1>
                            <h5 class="mb-3"><i class="bi bi-calendar me-2"></i>2 December</h5>
                            <h5 class="mb-3"><i class="bi bi-clock me-2"></i>6:00 am</h5>
                            <h5 class="mb-3"><i class="bi bi-geo-alt-fill me-2"></i>Sayran</h5>
                            <button type="submit" class="btn btn-primary mb-3">{{ $t('Sign up') }}</button>
                        </div>
                    </div>
                </div>
                <div class="carousel-item" data-bs-interval="10000">
                    <div class="row ms-3 me-3 border-top">
                        <div class="col-md-6 text-center">
                            <img src="../assets/Kolsai-Lakes.jpg" class="my-3 img-fluid">
                        </div>
                        <div class="col-md-6 my-auto ps-5">
                            <h1 class="mb-3">Almaty Kolsai Lake</h1>
                            <h5 class="mb-3"><i class="bi bi-calendar me-2"></i>2 December</h5>
                            <h5 class="mb-3"><i class="bi bi-clock me-2"></i>6:00 am</h5>
                            <h5 class="mb-3"><i class="bi bi-geo-alt-fill me-2"></i>Sayran</h5>
                            <button type="submit" class="btn btn-primary mb-3">{{ $t('Sign up') }}</button>
                        </div>
                    </div>
                </div>
                <div class="carousel-item" data-bs-interval="10000">
                    <div class="row ms-3 me-3 border-top">
                        <div class="col-md-6 text-center">
                            <img src="../assets/Kolsai-Lakes.jpg" class="my-3 img-fluid">
                        </div>
                        <div class="col-md-6 my-auto ps-5">
                            <h1 class="mb-3">Almaty Kolsai Lake</h1>
                            <h5 class="mb-3"><i class="bi bi-calendar me-2"></i>2 December</h5>
                            <h5 class="mb-3"><i class="bi bi-clock me-2"></i>6:00 am</h5>
                            <h5 class="mb-3"><i class="bi bi-geo-alt-fill me-2"></i>Sayran</h5>
                            <button type="submit" class="btn btn-primary mb-3">{{ $t('Sign up') }}</button>
                        </div>
                    </div>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    
        

    </div>
</div>


</template>


<script>

export default {
computed: {
    isLoggedIn: function () { return this.$store.getters.isAuthenticated; }
},
data() {
    return {
        user: {
            name: "Some Name",
            lastName: "Some Last Name"
        }
    }
},
methods: {
    async fetchUser() {
        
        let result = null;

        await this.axios.get("https://randomuser.me/api/").then( (response) => {
            result = response;
        });

        this.user.name = result.data.results[0].name.first;
        this.user.lastName = result.data.results[0].name.last;
    }
},
async mounted() {
    await this.fetchUser();
    
}
}
</script>

<style scoped>

img{
width: 80%;
}
.carousel{
background-color: #FDF7F7;
}
.carousel-control-next, .carousel-control-prev {
width: 5% !important;
}
.banner-home{
background-image: url("../assets/Background.png");
min-height: 100vh !important;
background-position: center;
background-repeat: no-repeat;
background-size: cover;
}
.white{
color: #FFF !important;
}
span, .btn-secondary{
font-size: 32px;
}
.btn-green{
    background-color: #1C5E3C !important;
	border-color: #1C5E3C !important;
}
hr{
    border: 3px solid #ECECEC !important;
    border-radius: 18px;
    opacity: 1;
}
</style>