<template>
    <div class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-4 pt-lg-5 pt-4">
            <form class="text-center mt-5 mx-auto">
                <h2 class="pt-3">{{ $t('Passenger Information') }}</h2>
                    <div class="mb-3">
                        <input type="firstname" class="form-control mx-auto" id="firstname" placeholder="Vasia">
                    </div>
                    <div class="mb-3">
                        <input type="lastname" class="form-control mx-auto" id="lastname" placeholder="Pupkin">
                    </div>
                    <div class="mb-3">
                        <input type="lastname" class="form-control mx-auto" id="lastname" placeholder="Poluektovich">
                    </div>
                    <select class="mx-auto form-select mb-3">
                        <option selected disabled class="selected">{{ $t('Document Type') }}</option>
                        <option value="1" data-content="">{{ $t('Passport') }}</option>
                        <option value="2">{{ $t('Identity Card') }}</option>
                    </select>   
                    <div class="mb-3">
                        <input type="lastname" class="form-control mx-auto" id="lastname" placeholder="Document Number">
                    </div>
                <button type="submit" class="btn btn-primary mt-3 mb-3">{{ $t('Confirm') }}</button> <br/>
            </form>
        </div>
    </div>
</template>


<script>
</script>

<style scoped>

</style>