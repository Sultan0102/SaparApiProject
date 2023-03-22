<template>
    <div class="container-fluid pt-5">
        <div class="container mt-5">
            <h1 class="text-center">Almaty<i class="bi bi-caret-right-fill"></i>Kolsai lake tour</h1>
            <div class="row">
                <div class="col-md-6">
                    <h2 class="my-1">{{ $t('When?') }}</h2>
                    <h3 class="mb-4">25 April, 14:00</h3>
                    <h2 class="my-1">{{ $t('Where?') }}</h2>
                    <h3 class="mb-4">Sayran Terminal</h3>
                    <h2 class="my-1">{{ $t("What's interesting?") }}</h2>
                    <ul class="mb-4">
                        <li>Guided tour</li>
                        <li>Lunch break</li>
                        <li>Photoshoot time</li>
                        <li>Games</li>
                    </ul>
                </div>
                <div class="col-md-6 my-auto text-center">
                    <img src="../assets/Kolsai-Lakes.jpg" class="img-fluid w-75">
                </div>
            </div>
            <div class="text-center">
            <h2 class="my-1 mt-4">{{ $t('Still have questions?') }}</h2>
            <h3 class="mb-4">{{ $t('Contact our tour manager') }}: 87089802877</h3>
            <router-link class="nav-link" aria-current="page" to="/tickets"><button type="button" class="btn btn-primary mb-5">{{ $t('Go back') }}</button></router-link>
            
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
.container{
    max-width: 800px;
    background-color: #FFFFFF;
}
h3, li{
    opacity: 0.8;
}
.img-fluid{
    box-shadow: 12px 12px #1C5E3C;
}
</style>


