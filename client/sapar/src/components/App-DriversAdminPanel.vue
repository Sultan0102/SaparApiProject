<template>  
    <div class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9">
                    <div class="mx-auto mb-3 ms-5 mt-4">
                        <div class="input-group">
                            <input v-model="filters.id" type="search" class="form-control" :placeholder="$t('By id:')" aria-label="Search">
                            <button class="btn search" type="button" @click="searchDriverById"><i class="bi bi-search"></i></button>
                        </div>
                        <div class="input-group mt-4">
                            <input v-model="filters.name" type="search" class="form-control" :placeholder="$t('By name:')" aria-label="Search">
                            <button class="btn search" type="button" @click="searchDriverByName"><i class="bi bi-search"></i></button>
                        </div>
                        <div v-for="driver in drivers" 
                        class="input-group mt-4">
                            <div class="form-control">{{ getFormattedDriver(driver) }}</div>
                            <button class="btn search" type="button" @click="editDriverClick(driver.id)"><i class="bi bi-pencil-square"></i></button>
                        </div>
                    </div>
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col" @click="filterApplications('Type')">{{ $t('Type') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col" @click="filterApplications('Name')">{{ $t('Name') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col" @click="filterApplications('Date')">{{ $t('Date') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="application in applications"
                                    @click="viewApplication(application)"
                                >
                                    <th>{{ application.type.name }}</th>
                                    <td>{{ `${application.senderUser.firstName} ${application.senderUser.lastName}` }}</td>
                                    <td>{{ getFormattedApplicationDate(application.creationDate) }}</td>
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
import UserService from "@/services/UserService";
import ApplicationService from "@/services/ApplicationService"


export default{
    components: {
        Navigation
    },
    data() {
        return {
            drivers: [],
            filters: {
                id: null,
                name: null
            },
            sortings: {
                date: 'asc',
                name: 'asc',
                type: 'asc'
            },
            applications: []
        }
    },
    computed: {
       
    },
    methods: {

        viewApplication(application) {
            if(application.type.id == 4) {
                this.$router.push({ name: 'ViewNewRouteApplication', params: { applicationId: application.id }})
                return;
            }

            if(application.type.id == 3) {
                this.$router.push({ name: 'ViewSabbaticalApplication', params: { applicationId: application.id }})
                return;
            }

            if(application.type.id == 5) {
                this.$router.push({ name: 'ViewRemoveRouteApplication', params: { applicationId: application.id }})
                return;
            }

        },

        filterApplications(sortColumn) {
            switch(sortColumn) {
                case 'Type':
                    if(this.sortings.type == 'asc') {
                        this.applications = this.applications.sort((a,b)=> a.type.name > b.type.name ? -1 : 1)
                        this.sortings.type = 'desc'
                    }
                    else {
                        this.applications = this.applications.sort((a,b)=> a.type.name < b.type.name ? -1 : 1)
                        this.sortings.type = 'asc'
                    }
                break;

                case 'Date':
                    if(this.sortings.date == 'asc') {
                        this.applications = this.applications.sort((a,b)=> a.creationDate > b.creationDate ? -1 : 1)
                        this.sortings.date = 'desc'
                    }
                    else {
                        this.applications = this.applications.sort((a,b)=> a.creationDate < b.creationDate ? -1 : 1)
                        this.sortings.date = 'asc'
                    }
                break;

                case 'Name':
                    if(this.sortings.name == 'asc') {
                        this.applications = this.applications.sort((a,b)=> a.senderUser.firstName > b.senderUser.firstName ? -1 : 1)
                        this.sortings.name = 'desc'
                    }
                    else {
                        this.applications = this.applications.sort((a,b)=> a.senderUser.firstName < b.senderUser.firstName ? -1 : 1)
                        this.sortings.name = 'asc'
                    }
                break;
                default:
                break;
            }
        },


        async getApplications() {
            await ApplicationService.getDriverApplications().then(
                (data)=> {
                    this.applications = data;
                }
            )
        },

        getFormattedApplicationDate(dateIsoStr) {
            let date = new Date(dateIsoStr)
            let day = date.getDay()
            let month = date.getMonth()
            
            if (day < 10) day = '0'+day
            if (month < 10) month = '0'+month
            

            return `${day}.${month}.${date.getFullYear()}`
        },

        getFormattedDriver(driver) {
            if (driver == null)
                return ''
            
            return `${driver.id} / ${driver.user.firstName} ${driver.user.lastName} / ${driver.yearExperience}`
        },

        async searchDriverById() {
            const id = this.filters.id
            if(id==null || id.length == 0)
                return;
            
            this.filters.name = null
            await UserService.retreiveDriverById(id).then(
                (data)=> {
                    if (this.drivers.every(d => d.id != data.id))
                        this.drivers.push(data);
                    else {
                        this.drivers = [data]
                    }
                },
                (error)=>{
                    if(error.response.status == 404) {
                        this.$notify({
                            type: "warning",
                            title: "Not Found",
                            text: "No driver with such Id!"
                        })
                    } else {
                        this.$notify({
                            type: "error",
                            title: "Error",
                            text: error.message
                        })
                    }
                }
            )
        },
        async searchDriverByName() {
            const name = this.filters.name
            if(name==null || name.length == 0)
                return;
            
            this.filters.id = null
            await UserService.retreiveDriverByName(name).then(
                (data)=> {
                    this.drivers = data;
                },
                (error)=>{
                    if(error.response.status == 404) {
                        this.$notify({
                            type: "warning",
                            title: "Not Found",
                            text: "No driver with such Id!"
                        })
                    } else {
                        this.$notify({
                            type: "error",
                            title: "Error",
                            text: error.message
                        })
                    }
                }
            )
        },
        editDriverClick(id) {
            if (id == null) {
                this.$notify({
                    type: "error",
                    title: "Error",
                    text: "You cannot edit without picking driver!"
                })
                return;
            }

            this.$router.push({
                name: "DriverProfile",
                params: { driverId: id }
            })
        }
    },

    mounted() {
        this.getApplications()
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