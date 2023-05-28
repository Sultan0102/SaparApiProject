<template>
    <div id="profile" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="col-lg-5 mx-auto pt-5">
                    <div class="applications-list">
                        <h2 class="my-3">{{ $t('Applications') }}</h2>
                        <ul class="list-group text-start">
                            <li v-for="application in applications"
                            class="list-group-item list-group-item-action ps-5 "
                            @click="viewApplication(application)"
                            >
                                <AppApplication 
                                :application="application"
                                />
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
import AppApplication from "@/components/App-Application.vue"
import ApplicationService from '@/services/ApplicationService';
import TokenService from '@/services/TokenService';


export default {
    components: {
        AppApplication
    },
    data() {
        return {
            applications: [],
        }
    },
    methods: {
        viewApplication(application) {
            if(application.type == 2)
            {
                this.$router.push({
                    name: 'ViewGuideFireApplication',
                    params: { applicationId: application.id }
                })
                return;
            }

            if(application.type == 1) {
                this.$router.push({
                    name: 'ViewGuideHireApplication',
                    params: { applicationId: application.id }
                })
            }
        },
        async getUserApplications() {
            let userId = TokenService.getUser().id;
            const criteria = {
                userId: userId
            }

            await ApplicationService.getUserApplications(criteria).then(
                (data)=> {
                    this.applications = data
                }
            )
        }
    },
    async mounted() {
        await this.getUserApplications();
    }
}
</script>

<style scoped>
.applications-list{
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
