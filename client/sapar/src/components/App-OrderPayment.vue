<template>
    <div class="container-fluid my-5 py-5">
        <div class="container mt-lg-5 mt-4 pt-lg-5 pt-4">
            <form class="text-center mt-5 mx-auto">
                <h2 class="pt-3">{{ $t('Checkout Details') }}</h2>
                <div class="mt-3 py-4">
                    <select class="mx-auto form-select mb-5">
                        <option selected disabled class="selected">{{ $t('Payment Method') }}</option>
                        <option value="1">Kaspi</option>
                        <option value="2">Halyk</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary my-5">{{ $t('Confirm') }}</button>
            </form>
        </div>
    </div>
</template>


<script>
</script>

<style scoped>
</style>