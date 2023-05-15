<template>
    <div class="container-fluid my-5 py-5">
        <div class="container mt-lg-5 mt-4 pt-lg-5 pt-4">
            <form class="text-center mt-5 mx-auto">
                <h2 class="pt-3">{{ $t('Order Number') }}</h2>
                <div class="mt-3 py-4">
                    <h1>3546520110</h1>
                </div>
                <button type="submit" class="btn btn-primary mt-3 mb-5" @click="this.$router.push({path: '/'})">{{ $t('Go to Kaspi.kz') }}</button> <br/>
            </form>
        </div>
    </div>
    
</template>


<script>
</script>

<style scoped>
</style>