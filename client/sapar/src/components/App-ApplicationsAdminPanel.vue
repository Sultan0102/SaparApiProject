<template>  
    <div v-if="applications && applicationTypes" class="container-fluid py-5 mt-5">
        <div class="container">
            <div class="row">
                <Navigation/>
                <div class="col-xl-9">
                    <div class="container table-responsive">
                        <table class="table table-hover text-center">
                            <thead>
                                <tr>
                                    <th scope="col">
                                        <select v-model="sortings.type" class="form-select mx-auto" aria-label="Default select example" @change="filterSchedules('Type')">
                                            <option selected disabled value="0">{{ $t('Type') }}</option>
                                            <option v-for="applicationType in applicationTypes"
                                            :value="applicationType.id"
                                            >
                                                {{ applicationType.name }}
                                            </option>
                                        </select>
                                    </th>
                                    <th scope="col" @click="filterSchedules('Name')">{{ $t('Name') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col" @click="filterSchedules('Role')">{{ $t('Role') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col" @click="filterSchedules('Status')">{{ $t('Status') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col" @click="filterSchedules('Date')">{{ $t('Date') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>

                                <tr v-for="application in applications"
                                :key="application.id"
                                @click="openApplication(application)"
                                >
                                    <th>{{ application.type.name }}</th>
                                    <td>{{ `${application.senderUser.firstName} ${application.senderUser.lastName}` }}</td>
                                    <td>{{ getRoleName(application.senderUser.role) }}</td>
                                    <td>
                                        <i v-if="application.status.id == 1" class="bi bi-circle"></i>
                                        <i v-if="application.status.id == 2" class="bi bi-check-circle-fill"></i>
                                        <i v-if="application.status.id == 3" class="bi bi-x-circle"></i>
                                    </td>
                                    <td>
                                        {{ formattedApplicationDate(application) }}
                                    </td>
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
import ApplicationService from "@/services/ApplicationService";

export default{
    components: {
        Navigation
    },
    data() {
        return {
            applications: [],
            applicationTypes: [],
            sortings: {
                type: 0,
                name: 'asc',
                role: 'asc',
                status: 'asc',
                date: 'asc'

            }
        }
    },
    methods: {
        async getApplications() {
            await ApplicationService.retreiveWithDepth().then(
                (data)=> {
                    this.applications = data
                }
            )
        },
        async getApplicationTypes() {
            await ApplicationService.retreiveApplicationTypes().then(
                (data)=> {
                    this.applicationTypes = data
                }
            )
        },

        openApplication(application) {
            if(application.type.id == 1) {
                // go to HireGuide
                this.$router.push({
                    name: "ViewGuideHireAdminApplication",
                    params: { applicationId: application.id  }
                })
            }

            if(application.type.id == 2) {
                // go to Fire Guide
                this.$router.push({
                    name: "ViewGuideFireAdminApplication",
                    params: { applicationId: application.id  }
                })
            }

            if(application.type.id == 3) {
                // go to Sabbatical
                this.$router.push({
                    name: "ViewSabbaticalApplication",
                    params: { applicationId: application.id  }
                })
            }

            if(application.type.id == 4) {
                // go to NewRoute
                this.$router.push({
                    name: "ViewNewRouteApplication",
                    params: { applicationId: application.id  }
                })
            }

            if(application.type.id == 5) {
                // go to Remove Route
                this.$router.push({
                    name: "ViewRemoveRouteApplication",
                    params: { applicationId: application.id  }
                })
            }
            
        },

        getRoleName(roleId) {
            switch(roleId) {
                case 1: 
                return 'Admin';
                case 2: 
                return "Customer";
                case 3: 
                return "Guide";
                case 4: 
                return "Business Person";
                case 5: 
                return "Driver";
                default:
                return "Customer"
            }
        },
        getTimeZonedDateStr(dateStr) {
            let timeZonedDateStr = new Date(dateStr).toLocaleString('ru', {timeZone: 'Asia/Almaty'})
            
            return timeZonedDateStr;
        },
        formattedApplicationDate(application) {
            let timezonedDate = this.getTimeZonedDateStr(application.creationDate)
            
            return timezonedDate
        },

        filterSchedules(sortColumn) {
            switch(sortColumn) {
                case 'Type':
                    this.applications = this.applications.sort((a,b)=> {
                        if(a.type.id != this.sortings.type && b.type.id == this.sortings.type) return 1
                        if(a.type.id == this.sortings.type && b.type.id != this.sortings.type) return -1

                        return 0
                    })
                    
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

                case 'Role':
                    if(this.sortings.role == 'asc') {
                        this.applications = this.applications.sort((a,b)=> a.senderUser.role > b.senderUser.role ? -1 : 1)
                        this.sortings.role = 'desc'
                    }
                    else {
                        this.applications = this.applications.sort((a,b)=> a.senderUser.role < b.senderUser.role ? -1 : 1)
                        this.sortings.role = 'asc'
                    }
                break;

                case 'Status':
                    if(this.sortings.status == 'asc') {
                        this.applications = this.applications.sort((a,b)=> a.status.id > b.status.id ? -1 : 1)
                        this.sortings.status = 'desc'
                    }
                    else {
                        this.applications = this.applications.sort((a,b)=> a.status.id < b.status.id ? -1 : 1)
                        this.sortings.status = 'asc'
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
                default:
                break;
            }
        },
    },
    async mounted() {
        await this.getApplications()
        await this.getApplicationTypes()
        console.log(this.applicationTypes)
        console.log(this.applications)
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