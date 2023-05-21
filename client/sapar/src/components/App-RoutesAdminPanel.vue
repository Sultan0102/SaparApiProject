<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9 text-center">
                    <div class="mx-auto mb-3 ms-5 mt-4">
                        <div class="input-group">
                            <input type="search" class="form-control" :placeholder="$t('By schedule number:')" aria-label="Search">
                            <button class="btn search" type="button"><i class="bi bi-search"></i></button>
                        </div>
                    </div>
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col">{{ $t('Schedule') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('From') }} - {{ $t('To') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Departure - Arrival Time') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th>AB4958</th>
                                    <td>Almaty - Taraz</td>
                                    <td>10:40pm - 05:30pm</td>
                                </tr>
                                <tr>
                                    <th>AB4958</th>
                                    <td>Almaty - Taraz</td>
                                    <td>10:40pm - 05:30pm</td>
                                </tr>
                                <tr>
                                    <th>AB4958</th>
                                    <td>Almaty - Taraz</td>
                                    <td>10:40pm - 05:30pm</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <router-link class="nav-link" to="/new-route"><button type="submit" class="btn btn-primary mt-5">{{ $t('New') }}</button></router-link>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import Navigation from "@/components/App-NavigationAdminPanel.vue";

export default{
    components: {
        Navigation
    }
}
</script>

<style scoped>  
*{
	color: #1C5E3C;
}
th{
    padding-bottom: 1rem !important;
    min-width: 33.3% !important;
}
.filter-icon{
    width: 15px;
}
.input-group{
    max-width: 1300px;
}
.search{
    border-bottom-right-radius: 15px !important;
	border-top-right-radius: 15px !important;
    background-color: #FFF !important;
}
.form-control, .form-control-plaintext{
    border-bottom: none !important;
    border-radius: 15px;
}
</style>