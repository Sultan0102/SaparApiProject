<template>
    <div id="profile" class="container-fluid my-4">
        <div class="container mt-lg-3 mt-0 pt-lg-3 pt-0">
            <div class="align-items-center">
                    <div class="tours mx-auto mt-5">
                        <h2 class="py-3 text-center">{{ $t('Tours') }}</h2>
                        <ul class="list-group">
                            <li class="list-group-item list-group-item-action">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</li>
                            <li class="list-group-item list-group-item-action">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</li>
                            
                            <button type="button" class="btn btn-primary mx-auto mb-3 mt-5">{{ $t('See more') }}</button>
                        </ul>
                    </div>
                    <div class="tours mx-auto mt-5">
                        <h2 class="py-3 text-center">{{ $t('Guide applications') }}</h2>
                        <ul class="list-group">
                            <li class="list-group-item list-group-item-action">
                                <div class="row">
                                    <div class="col-6">Elvira Nugmanova R. <br/> Taraz - Almaty</div>
                                    <div class="col-6 text-end my-auto">Tue 2, 14:35</div>
                                </div>
                            </li>
                            <li class="list-group-item list-group-item-action">
                                <div class="row">
                                    <div class="col-6">Elvira Nugmanova R. <br/> Taraz - Almaty</div>
                                    <div class="col-6 text-end my-auto">Tue 2, 14:35</div>
                                </div>
                            </li>
                            
                            <button type="button" class="btn btn-primary mx-auto mb-3 mt-5">{{ $t('See more') }}</button>
                        </ul>
                    </div>
            </div>
            
        </div>
    </div>
</template>


<script>
</script>

<style scoped>
.tours{
    border-color: #1C5E3C !important;
	border-left-style: solid;
    border-left-width: 50px;
    background-color: #FFF;
    max-width: 500px;
}
.list-group-item{
    border: none !important;
    border-bottom: 1px solid #ECECEC !important;
}
</style>
