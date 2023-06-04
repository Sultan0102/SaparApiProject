<template>
<div v-if="businessPerson" class="container-fluid mb-4 pb-4">
        <div class="container mt-lg-4 mt-3 pt-lg-4 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto" @submit.prevent="verifyAccount">
                        <h2 class="pt-3">{{ $t('Guide information') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                            <input v-model="businessPerson.user.email" type="email" id="email" name="email" class="form-control" disabled readonly aria-describedby="emailHelp" placeholder="email@example.com">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="businessPerson.user.firstName" type="text" id="firstName" name="firstName" class="form-control" disabled readonly placeholder="Vasia">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="businessPerson.user.lastName" type="text" id="lastName" name="lastName" class="form-control" disabled readonly placeholder="Pupkin">
                        </div>

                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="businessPerson.binNumber" type="text" id="binNumber" name="binNumber" class="form-control" disabled readonly placeholder="Pupkin">
                        </div>

                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="businessPerson.companyName" type="text" id="companyName" name="companyName" class="form-control" disabled readonly placeholder="Company">
                        </div>

                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input v-model="businessPerson.legalAddress" type="text" id="legalAddress" name="legalAddress" class="form-control" disabled readonly placeholder="Address">
                        </div>
                        
                        <button class="btn btn-primary mb-3 mt-3">{{ $t('Verify') }}</button>
                        
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
import UserService from '@/services/UserService';

export default {
    props: ['businessPersonId'],
    data() {
        return {
            businessPerson: null
        }
    },
    methods: {
        async getBusinessPerson() {
            await UserService.retreiveBusinessPersonById(this.businessPersonId).then(
                (data)=> {
                    this.businessPerson = data
                }
            )
        },

        async verifyAccount() {
            console.log('verify');
            await UserService.verifyBusinessPerson(this.businessPerson.id).then(
                (data)=>{
                    this.$router.back();
                    this.$notify({
                        type: 'success',
                        title: 'Verify Business Person',
                        text: 'Successfully Verified Business Person!'
                    })
                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: 'Verify Business Person',
                        text: 'Error occured while verifying Business Person!'
                    })
                }
            )
        }
    },

    async mounted() {
        await this.getBusinessPerson()
    }
}

</script>

<style>

</style>