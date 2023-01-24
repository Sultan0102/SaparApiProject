<template>
    <div class="container-fluid py-5">
        <div class="container">
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
                                    <img src="../assets/Kolsai-Lakes.jpg" class="p-2 img-fluid">
                                </div>
                                <div class="col-md-6 my-auto">
                                    <div>
                                    <h1 class="">Almaty Kolsai Lake</h1>
                                    <p>2 December</p>
                                    <p>6:00 am</p>
                                    <p>Sayran</p>
                                    <div class="text-center">
                                        <button type="submit" class="btn btn-primary mb-3 ">{{ $t('Sign up') }}</button>
                                    </div>
                                    </div>
                                </div>
                            </div>
                    </div>
                    <div class="carousel-item" data-bs-interval="10000">
                        <div class="row ms-3 me-3 border-top">
                                <div class="col-md-6 text-center">
                                    <img src="../assets/Kolsai-Lakes.jpg" width="80%" class="p-2 img-fluid">
                                </div>
                                <div class="col-md-6 text-center my-auto">
                                    <div>
                                    <h1 class="">Almaty Kolsai Lake</h1>
                                    <p>2 December</p>
                                    <p>6:00 am</p>
                                    <p>Sayran</p>
                                    <button type="submit" class="btn btn-primary mb-3">Sign up</button>
                                    </div>
                                </div>
                            </div>
                    </div>
                    <div class="carousel-item" data-bs-interval="10000">
                        <div class="row ms-3 me-3 border-top">
                                <div class="col-md-6 text-center">
                                    <img src="https://www.journalofnomads.com/wp-content/uploads/2017/10/Kolsai-Lakes-1.jpg" width="80%" class="p-2 img-fluid">
                                </div>
                                <div class="col-md-6 text-center my-auto">
                                    <div>
                                    <h1 class="">Almaty Kolsai Lake</h1>
                                    <p>2 December</p>
                                    <p>6:00 am</p>
                                    <p>Sayran</p>
                                    <button type="submit" class="btn btn-primary mb-3">Sign up</button>
                                    </div>
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
</style>