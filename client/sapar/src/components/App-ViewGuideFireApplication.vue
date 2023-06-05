<template>
    <div v-if="application" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto mb-5 pb-5">
                        <h2 class="pt-3 pb-3">{{ $t('Firing Application') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-4 ms-sm-5"></i>
                            <input :value="application.email" type="email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input :value="application.firstName" type="text" id="firstName" name="firstName" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input :value="application.lastName" type="text" id="lastName" name="lastName" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-calendar my-auto ms-4 ms-sm-5"></i>
                            <input :value="formattedEffectiveFromDate" type="text" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-caret-down-fill ms-4 ms-sm-5 my-auto"></i>
                            <input v-model="application.firingReason" type="text" class="form-control" readonly disabled>
                        </div>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import ApplicationService from '@/services/ApplicationService';


export default {
    props: ['applicationId'],
    data() {
        return {
            application: {
                email: null,
                firstName: null,
                lastName: null,
                effectiveFrom: '',
                firingReason: null,
            },
        }
    },
    computed: {
        formattedEffectiveFromDate: function() {
            let date = new Date(this.application.effectiveFrom)

            return `${date.getDate()}.${date.getMonth()}.${date.getFullYear()}`
        },
    },
    methods: {

        async getApplication() {
            await ApplicationService.retreive(this.applicationId).then(
                (data)=> {
                    this.application = data.applicationData
                }
            )
        },


    },
    async mounted() {
        await this.getApplication();
    }
}

</script>

<style scoped>
.form-select{
    background-image: none;
}
</style>
