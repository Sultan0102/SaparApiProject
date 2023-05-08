<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9">
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col">
                                    <select class="form-select mx-auto" aria-label="Default select example">
                                        <option selected>{{ $t('Type') }}</option>
                                        <option value="1">One</option>
                                        <option value="2">Two</option>
                                        <option value="3">Three</option>
                                    </select></th>
                                    <th scope="col">{{ $t('Name') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Role') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Status') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Date') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th>Vacation Application</th>
                                    <td>Vasya Pupkin</td>
                                    <td>Driver</td>
                                    <td><i class="bi bi-circle"></i></td>
                                    <td>20.04.2023</td>
                                </tr>
                                <tr>
                                    <th>Vacation Application</th>
                                    <td>Vasya Pupkin</td>
                                    <td>Driver</td>
                                    <td><i class="bi bi-check-circle-fill"></i></td>
                                    <td>20.04.2023</td>
                                </tr>
                                <tr>
                                    <th>Vacation Application</th>
                                    <td>Vasya Pupkin</td>
                                    <td>Driver</td>
                                    <td><i class="bi bi-circle"></i></td>
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
.form-select{
    background-color: #ECECEC !important;
    padding: 0 !important;
    border: 0 !important;
    width: 50%;
}
</style>