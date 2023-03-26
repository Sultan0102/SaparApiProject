<template>
    <div class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto">
                        <h2 class="pt-3">{{ $t('Application') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-4 ms-sm-5"></i>
                            <input type="email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" placeholder="email@example.com">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input type="text" id="firstName" name="firstName" class="form-control" placeholder="Vasia">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input type="text" id="lastName" name="lastName" class="form-control" placeholder="Pupkin">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-calendar my-auto ms-4 ms-sm-5"></i>
                            <div class="form-control"><VueDatePicker v-model="date" model-auto position="left" placeholder="Effective from" hide-input-icon /></div>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-caret-down-fill ms-4 ms-sm-5 my-auto"></i>
                            <select class="form-select">
                                <option selected disabled class="selected">{{ $t('Choose a tour') }}</option>
                                <option value="1" data-content="">{{ $t('Tour Kolsai - Almaty') }}</option>
                                <option value="2">{{ $t('Tour Kolsai - Almaty') }}</option>
                            </select>   
                        </div>
                        <button type="submit" class="btn btn-primary mt-5 mb-3 disabled">{{ $t('Approve') }}</button> <br/>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>

</script>

<style scoped>
.form-select{
    background-image: none;
}
</style>
