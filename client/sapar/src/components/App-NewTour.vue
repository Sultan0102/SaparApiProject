<template>
    <div class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto">
                        <h2 class="pt-3">{{ $t('Create a tour') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-geo-alt-fill my-auto ms-4 ms-sm-5"></i>
                            <input type="text" id="source" name="source" class="form-control" :placeholder="$t('From')">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-geo-alt-fill my-auto ms-4 ms-sm-5"></i>
                            <input type="text" id="destination" name="destination" class="form-control" :placeholder="$t('To')">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-clock my-auto ms-4 ms-sm-5"></i>
                            <div class="form-control"><VueDatePicker v-model="time" model-auto position="left" time-picker range :placeholder="$t('Duration')" hide-input-icon/></div>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-pencil-fill mt-1 mb-auto ms-4 ms-sm-5"></i>
                            <textarea class="form-control" id="description" :placeholder="$t('Description')" rows="1"></textarea>
                        </div>

                        <button type="submit" class="btn btn-primary mt-5 mb-3 disabled">{{ $t('Create') }}</button> <br/>
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
textarea {
	resize: vertical;
    height: 17px;
}
</style>
