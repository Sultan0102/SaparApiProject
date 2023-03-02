<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-5">
                <h2 class="pt-3">{{ $t('Checkout Details') }}</h2>

                <div class="dropdown mt-3">
                    <button class="btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                        {{ $t('Payment Method') }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Kaspi</a></li>
                        <li><a class="dropdown-item" href="#">Halyk</a></li>
                    </ul>
                </div>
                <button type="submit" class="btn btn-primary mt-3 mb-3">{{ $t('Confirm') }}</button> <br/>
            </form>
        </div>
    </div>
</template>


<script>
</script>

<style scoped>
p{
    color:#1C5E3C;
    padding-bottom: 0px !important;
}
.alert{
    margin: auto;
    width: 50%;
}
form{
	width: 50%;
}
.btn-secondary {
  color: #6c757d !important;
  background-color: #fff;
  border: none !important;
  border-color: #1C5E3C;
  border-bottom: 1px solid !important;
}
.btn-check:focus + .btn-secondary, .btn-secondary:focus {
  box-shadow: none !important;
}
.dropdown-item{
    color: #1C5E3C !important;
}
</style>