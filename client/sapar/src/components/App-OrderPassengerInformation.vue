<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-5">
                <h2 class="pt-3">{{ $t('Passenger Information') }}</h2>
                    <div class="mb-3">
                        <input type="firstname" class="form-control text-center" id="firstname" placeholder="Vasia">
                    </div>
                    <div class="mb-3">
                        <input type="lastname" class="form-control text-center" id="lastname" placeholder="Pupkin">
                    </div>
                    <div class="mb-3">
                        <input type="lastname" class="form-control text-center" id="lastname" placeholder="Poluektovich">
                    </div>
                    <div class="mb-3">
                        <div class="dropdown mt-3">
                            <button class="btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                                {{ $t('Document Type') }}
                            </button>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#">{{ $t('Passport') }}</a></li>
                                <li><a class="dropdown-item" href="#">{{ $t('Identity Card') }}</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="mb-3">
                        <input type="lastname" class="form-control text-center" id="lastname" placeholder="Document Number">
                    </div>
                <button type="submit" class="btn btn-primary mt-3 mb-3">{{ $t('Confirm') }}</button> <br/>
            </form>
        </div>
    </div>
</template>


<script>
</script>

<style scoped>
*{
    color:#1C5E3C;
}
p{
    padding-bottom: 0px !important;
}
.alert{
    margin: auto;
    width: 50%;
}
form{
	max-width: 600px;
}
.btn-secondary {
    color:#6c757d !important;
    background-color: #fff;
    border: none !important;
    border-bottom: 1px solid !important;
    width: 80% !important;
}
.btn-check:focus + .btn-secondary, .btn-secondary:focus {
  box-shadow: none !important;
}
.dropdown-item{
    color: #1C5E3C !important;
}
</style>