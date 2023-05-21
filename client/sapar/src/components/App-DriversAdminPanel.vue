<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9">
                    <div class="mx-auto mb-3 ms-5 mt-4">
                        <div class="input-group">
                            <input type="search" class="form-control" :placeholder="$t('By id:')" aria-label="Search">
                            <button class="btn search" type="button"><i class="bi bi-search"></i></button>
                        </div>
                        <div class="input-group mt-4">
                            <input type="search" class="form-control" :placeholder="$t('By name:')" aria-label="Search">
                            <button class="btn search" type="button"><i class="bi bi-search"></i></button>
                        </div>
                        <div class="input-group mt-4">
                            <div class="form-control">298392 / Vasya Pupkin / 2 years</div>
                            <button class="btn search" type="button"><i class="bi bi-pencil-square"></i></button>
                        </div>
                    </div>
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col">{{ $t('Type') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Name') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Date') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th>Vacation Application</th>
                                    <td>Vasya Pupkin</td>
                                    <td>20.04.2023</td>
                                </tr>
                                <tr>
                                    <th>Vacation Application</th>
                                    <td>Vasya Pupkin</td>
                                    <td>20.04.2023</td>
                                </tr>
                                <tr>
                                    <th>Vacation Application</th>
                                    <td>Vasya Pupkin</td>
                                    <td>20.04.2023</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
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