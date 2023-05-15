<template>
    <div class="container-fluid mb-4 pb-4">
        <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto">
                        <h2 class="pt-3">{{ $t('Guide information') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                            <input type="email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" placeholder="email@example.com">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" id="firstName" name="firstName" class="form-control" placeholder="Vasia">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" id="lastName" name="lastName" class="form-control" placeholder="Pupkin">
                        </div>
                        <h2 class="py-3 text-center">{{ $t('Employment History') }}</h2>
                        <ul class="list-group mb-3">
                            <li class="list-group-item list-group-item-action">
                                <div class="row ms-3">
                                    <div class="col-1"><i class="bi bi-geo-alt-fill"></i></div>
                                    <div class="col-6 text-start">
                                        <h5>Sweet Tourism KZ</h5>
                                        <h6 class="ms-3">2019-2020<br/>Guide</h6>
                                    </div>
                                </div>
                            </li>
                            <li class="list-group-item list-group-item-action">
                                <div class="row ms-3">
                                    <div class="col-1"><i class="bi bi-geo-alt-fill"></i></div>
                                    <div class="col-6 text-start">
                                        <h5>Sweet Tourism KZ</h5>
                                        <h6 class="ms-3">2021-2022<br/>Guide manager</h6>
                                    </div>
                                </div>
                            </li>
                        </ul>

                        <button class="btn btn-secondary mb-3 mt-5"><i class="bi bi-file-earmark white me-2"></i>{{ $t('Upload CV') }}</button><br/>
                        <button class="btn btn-primary mb-3 mt-3">{{ $t('Log out') }}</button>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>

</script>

<style scoped>
.list-group-item{
    border: none !important;
    border-bottom: 1px solid #ECECEC !important;
}
i{
    font-size: 24px;
}
.btn-secondary{
    border-radius: 0px !important;
	background: none !important;
	border-color: #1C5E3C !important;
	border-width: 2px;
    color: #1C5E3C !important;
    min-width: 300px;
    font-size: 24px;
}
h6{
    opacity: 0.5;
}
</style>
