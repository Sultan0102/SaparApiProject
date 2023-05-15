<template>
    <div class="container-fluid py-5 mt-5">
        <div class="container mt-3 pb-5 mb-5">
            <h2 class="text-center">{{ $t('SAPAR IN NUMBERS') }}:</h2>
            <div class="row align-items-center border-top mt-2 pt-4">
                <div class="col-md-4 text-center">
                    <h1>247</h1>
                    <h5>{{ $t('Bus routes operated') }}</h5>
                </div>
                <div class="col-md-4 text-center">
                    <h1>154</h1>
                    <h5>{{ $t('Guided tours operated') }}</h5>
                </div>
                <div class="col-md-4 text-center">
                    <h1>352</h1>
                    <h5>{{ $t('Business partners') }}</h5>
                </div>
            </div>
            <h2 class="text-center mt-3">{{ $t('Sapar is not just a ride. It is an experience') }}!</h2>
            <div class="border-top mt-2 pt-4">
                <div class="text-center">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="row align-items-center swap-container">
                    <div class="col-md-5 text-md-end text-center mb-5 mb-md-0">
                        <img src="../assets/Cake.svg" class="person">
                    </div>
                    <div class="col-md-7 text-md-start text-center mt-5 mt-md-0">
                        <h3>{{ $t('89% of our customers returned to us again') }}</h3>
                        <h3 class="light-green">{{ $t('11% of people did not') }}</h3>
                    </div>
                </div>
            </div>
            <h2 class="text-center">{{ $t('MORE NUMBERS') }}:</h2>
            <div class="row align-items-center border-top mt-2 pt-5">
                <div class="col-md-4 text-center">
                    <h1>500</h1>
                    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-bus-front" viewBox="0 0 16 16">
                        <path d="M5 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm8 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0Zm-6-1a1 1 0 1 0 0 2h2a1 1 0 1 0 0-2H7Zm1-6c-1.876 0-3.426.109-4.552.226A.5.5 0 0 0 3 4.723v3.554a.5.5 0 0 0 .448.497C4.574 8.891 6.124 9 8 9c1.876 0 3.426-.109 4.552-.226A.5.5 0 0 0 13 8.277V4.723a.5.5 0 0 0-.448-.497A44.303 44.303 0 0 0 8 4Zm0-1c-1.837 0-3.353.107-4.448.22a.5.5 0 1 1-.104-.994A44.304 44.304 0 0 1 8 2c1.876 0 3.426.109 4.552.226a.5.5 0 1 1-.104.994A43.306 43.306 0 0 0 8 3Z"/>
                        <path d="M15 8a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1V2.64c0-1.188-.845-2.232-2.064-2.372A43.61 43.61 0 0 0 8 0C5.9 0 4.208.136 3.064.268 1.845.408 1 1.452 1 2.64V4a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1v3.5c0 .818.393 1.544 1 2v2a.5.5 0 0 0 .5.5h2a.5.5 0 0 0 .5-.5V14h6v1.5a.5.5 0 0 0 .5.5h2a.5.5 0 0 0 .5-.5v-2c.607-.456 1-1.182 1-2V8ZM8 1c2.056 0 3.71.134 4.822.261.676.078 1.178.66 1.178 1.379v8.86a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 11.5V2.64c0-.72.502-1.301 1.178-1.379A42.611 42.611 0 0 1 8 1Z"/>
                    </svg>
                    <p class="pt-3">{{ $t('Bus routes operated') }}</p>
                </div>
                <div class="col-md-4 text-center">
                    <h1>500</h1>
                    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                        <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                    </svg>
                    <p class="pt-3">{{ $t('New routes organized') }}</p>
                </div>
                <div class="col-md-4 text-center">
                    <h1>500</h1>
                    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-person-fill-gear" viewBox="0 0 16 16">
                        <path d="M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm-9 8c0 1 1 1 1 1h5.256A4.493 4.493 0 0 1 8 12.5a4.49 4.49 0 0 1 1.544-3.393C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4Zm9.886-3.54c.18-.613 1.048-.613 1.229 0l.043.148a.64.64 0 0 0 .921.382l.136-.074c.561-.306 1.175.308.87.869l-.075.136a.64.64 0 0 0 .382.92l.149.045c.612.18.612 1.048 0 1.229l-.15.043a.64.64 0 0 0-.38.921l.074.136c.305.561-.309 1.175-.87.87l-.136-.075a.64.64 0 0 0-.92.382l-.045.149c-.18.612-1.048.612-1.229 0l-.043-.15a.64.64 0 0 0-.921-.38l-.136.074c-.561.305-1.175-.309-.87-.87l.075-.136a.64.64 0 0 0-.382-.92l-.148-.045c-.613-.18-.613-1.048 0-1.229l.148-.043a.64.64 0 0 0 .382-.921l-.074-.136c-.306-.561.308-1.175.869-.87l.136.075a.64.64 0 0 0 .92-.382l.045-.148ZM14 12.5a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0Z"/>
                    </svg>
                    <p>{{ $t('Workers employed') }}</p>
                </div>
            </div>
            <div class="row align-items-center mt-2 pt-4">
                <div class="col-md-6 text-center">
                    <form class="text-center message">
                        <h3 class="my-3 pt-4">{{ $t('Tell us about your experience') }}!</h3>
                        <div class="mx-auto">
                            <input type="email" class=" form-control mx-auto" id="exampleInputEmail1" aria-describedby="emailHelp" :placeholder="$t('Email')" :disabled="editMode" :readonly="editMode">
                        </div>
                        <textarea class="form-control mx-auto" :placeholder="$t('Review')" id="review" rows="5"></textarea>
                        <button type="submit" class="btn btn-primary my-3">{{ $t('Send') }}</button>
                    </form>
                </div>
                <div class="col-md-6">
                    <img src="../assets/telework.png" class="img-fluid">
                </div>
            </div>
            <h2 class="text-center">{{ $t('PEOPLE ABOUT US') }}:</h2>
            <div class="row align-items-center border-top mt-2 pt-4">
                <div class="col-lg-4 text-center">
                    <img src="../assets/profile-photo.png" class="mb-3 person">
                </div>
                <div class="col-lg-8 message p-5">
                    <h2>{{ $t('Katira') }}</h2>
                    <h4>{{ $t('Ive bought here my first bus tour. I didnt think bus tourism was a thing before that, haha! But Im glad I visited Kolsai with Sapar. Really opened my eyes on how many places there are to visit in Kazakhstan.') }}</h4>
                </div>
            </div>
            <div class="row align-items-center mt-2 pt-4 swap-lg-container">
                <div class="col-lg-8 message p-5">
                    <h2>{{ $t('Katira') }}</h2>
                    <h4>{{ $t('Ive bought here my first bus tour. I didnt think bus tourism was a thing before that, haha! But Im glad I visited Kolsai with Sapar. Really opened my eyes on how many places there are to visit in Kazakhstan.') }}</h4>
                </div>
                <div class="col-lg-4 text-center">
                    <img src="../assets/profile-photo.png" class="mb-3 person">
                </div>
            </div>
        </div>
    </div>
</template>


<script>

</script>

<style scoped>
*{
    color: #1C5E3C;
}
h1{
    font-size: 100px !important;
}
.border-top{
	border-top: 2px solid #1C5E3C !important;
}
.message{
    background-color: #FFF;
    border-radius: 50px;
}
.form-control:focus {
  box-shadow: none !important;
}
button{
    color: #FFF;
}
textarea{
    background-image: -webkit-linear-gradient(left, white 0, transparent 0), -webkit-linear-gradient(right, white 0, transparent 0), -webkit-linear-gradient(white 30px, #ccc 30px, #ccc 31px, white 31px);
    background-repeat: repeat-y;
    background-size: 100% 100%, 100% 100%, 100% 31px;
    line-height: 31px;
}
form{
	max-width: 600px;
	border-left-style: none;
    border-left-width: none;
}
.person{
    width: 35vh;
    max-width: 400px;
}
.light-green{
    color: #57896F !important;
}
</style>
