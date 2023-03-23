<template>
    <div id="profile" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="col-lg-5 mx-auto pt-5">
                    <div class="order-history">
                        <h2 class="my-3">{{ $t('Applications') }}</h2>
                        <ul class="list-group text-start">
                            <li class="list-group-item list-group-item-action ps-5 ">
                                <div class="row">
                                    <div class="col-10">Active Firing Application <br/> Firing Vasya P. from Tour KZ5960</div>
                                    <div class="spinner-border col-2 mx-auto my-auto" role="status">
                                        <span class="visually-hidden">Loading...</span>
                                    </div>
                                </div>
                            </li>
                            <li class="list-group-item list-group-item-action ps-5 ">
                                <div class="row">
                                    <div class="col-10">Active Firing Application <br/> Firing Vasya P. from Tour KZ5960</div>
                                    <div class="col-2 text-center my-auto">
                                        <i class="bi bi-check-circle-fill"></i>
                                    </div>
                                </div>
                            </li>
                            <button type="button" class="btn btn-primary mx-auto mb-3 mt-5">{{ $t('See more') }}</button>
                        </ul>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
</script>

<style scoped>
.order-history{
    border-color: #1C5E3C !important;
	border-top-style: solid;
    border-top-width: 50px;
    background-color: #FFF;

}
.list-group-item{
    border: none !important;
    border-bottom: 1px solid #ECECEC !important;
}
.bi-check-circle-fill{
    font-size: 2rem !important;
}
</style>
