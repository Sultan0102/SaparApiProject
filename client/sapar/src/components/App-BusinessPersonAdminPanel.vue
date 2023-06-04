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
                                    <th scope="col">{{ $t('BIN') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Company Name') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Name') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                    <th scope="col">{{ $t('Date') }}<img src="../assets/filter.svg" class="filter-icon ms-2"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="person in businessPeople"
                                    @click="viewBusinessPerson(person)"
                                >
                                    <td>{{ person.binNumber }}</td>
                                    <td>{{ person.companyName }}</td>
                                    <td>{{ person.user.firstName + ' ' + person.user.lastName }}</td>
                                    <td>{{ getFormattedDateStr(person.user.creationDate) }}</td>
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
            businessPeople: [],
        }
    },
    methods: {

        viewBusinessPerson(person) {
            this.$router.push({
                name: 'BusinessPersonVerify',
                params: { businessPersonId: person.id }
            })
        },


        async getBusinessPeople() {
            await UserService.retreiveBusinessPersons().then(
                (data)=> {
                    this.businessPeople = data
                }
            )
        },

        getFormattedDateStr(dateStr) {
            let formattedDate = new Date(dateStr).toLocaleDateString('ru')
            return formattedDate
        }

    },

    async mounted() {
        await this.getBusinessPeople()
        console.log(this.businessPeople);
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