<template>
    <div class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row align-items-center tours mb-1 p-3">
                <div class="col-md-3">
                    <img src="../assets/Experience.png" class="img-fluid">
                </div>
                <div class="col-md-6">
                    <div class="ms-5 ms-md-0 mt-4 mt-md-0">
                        <h2 class="my-3">Vasya Pupkin</h2>
                        <h5 class="my-3"><i class="bi bi-clock"></i> Experience: 2 years</h5>
                        <h5 class="my-3"><i class="bi bi-geo-alt-fill"></i> Based in: Almaty</h5>
                        <h5 class="my-3 ms-4">Is involved in 4 guided tours</h5>
                    </div>
                </div>
                <div class="col-md-2 mt-auto mb-3">
                    <div class="ms-5 ms-md-0 mt-4 mt-md-0">
                        <button type="button" class="btn btn-primary">{{ $t('Modify') }}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>

</script>

<style scoped> 


.tours{
    background-color: #FFF;
}
.btn-primary{
	min-width: 150px;
    font-size: 24px;
}
</style>