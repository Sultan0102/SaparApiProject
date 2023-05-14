<template>
    <div v-if="tour && guide" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto" @submit.prevent="applyApplication">
                        <h2 class="pt-3">{{ $t('Application') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-4 ms-sm-5"></i>
                            <input v-model="application.email" type="email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" placeholder="email@example.com">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input v-model="application.firstName" type="text" id="firstName" name="firstName" class="form-control" placeholder="Vasia">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input v-model="application.lastName" type="text" id="lastName" name="lastName" class="form-control" placeholder="Pupkin">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-calendar my-auto ms-4 ms-sm-5"></i>
                            <div class="form-control">
                                <VueDatePicker 
                                v-model="application.effectiveFrom" 
                                hide-input-icon
                                placeholder="Effective from"
                                position="left"
                                :enable-time-picker="false"
                                ignore-time-validation
                                :allowed-dates="allowedDates" />
                            </div>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-caret-down-fill ms-4 ms-sm-5 my-auto"></i>
                            <select v-model="application.firingReason" class="form-select">
                                <option selected disabled class="selected">{{ $t('Firing reason') }}</option>
                                <option>{{ $t('Incompetence') }}</option>
                                <option>{{ $t('Time management') }}</option>
                                <option>{{ $t('Inappropriate behaviour') }}</option>
                                <option>{{ $t('Other') }}</option>
                            </select>   
                        </div>
                        <button type="submit" class="btn btn-primary mt-5 mb-3">{{ $t('Approve') }}</button> <br/>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import TourService from '@/services/TourService';
import UserService from '@/services/UserService';
import ApplicationService from '@/services/ApplicationService';
import TokenService from '@/services/TokenService';
import useVuelidate from '@vuelidate/core';
import { required } from '@vuelidate/validators';

export default {
    props: ['guideId', 'tourId'],
    setup() {
        return { v$: useVuelidate() }
    },
    data() {
        return {
            guide: null,
            tour: null,
            application: {
                email: null,
                firstName: null,
                lastName: null,
                effectiveFrom: '',
                firingReason: null,
            },
        }
    },
    validations() {
        return {
            application: {
                email: { required },
                firstName: { required },
                lastName: { required },
                effectiveFrom: {required},
                firingReason: { required }
            },
        }
    },
    computed: {
        allowedDates: function() {
            let schedules = this.tour.schedules.filter(s => new Date(s.beginDate) > new Date())
            schedules.push(new Date())
            return schedules.map(s => new Date(s.beginDate))
        },
    },
    methods: {
        async getTour() {
            await TourService.retreiveById(this.tourId).then(
                (data)=> {
                    this.tour = data
                }
            )
        },
        async getGuide() {
            await UserService.retreiveGuide(this.guideId).then(
                (data)=> {
                    this.guide = data
                }
            )

            this.application.email = this.guide.user.email;
            this.application.firstName = this.guide.user.firstName;
            this.application.lastName = this.guide.user.lastName;

        }, 

        async applyApplication() {
            console.log(this.application);
            const isValid = await this.v$.$validate()
            if(!isValid) {
                let errorMessages = ''
                this.v$.$errors.forEach((error)=> {
                    errorMessages+= `Field '${error.$property}'. ${error.$message} </br>`
                })

                this.$notify({
                    type: 'error',
                    title: 'Validation Error!',
                    text: errorMessages
                })
                return;
            }
            const userId = TokenService.getUser().id
            
            const applicationData = {
                guide: await this.getGuide().id,
                email: this.application.email,
                firstName: this.application.firstName,
                lastName: this.application.lastName,
                firingReason: this.application.firingReason,
                effectiveFrom: this.application.effectiveFrom.toISOString(),
                tour: this.tourId,
            }

            let applicationRequest = {
                senderUser: userId,
                receiverUser: this.guide.user.id,
                status: 1,
                type: 2,
                applicationData: applicationData,
                documents: []
            }

            await ApplicationService.createApplication(applicationRequest).then(
                (data)=> {
                    this.$router.push( {name: "BusinessTourList"} )
                    this.$notify({
                    type: 'success',
                    title: 'Application',
                    text: "Application was successfully created!"
                })
                },
                (error) => {
                    console.log(error.response)
                }
            )

        }

    },
    async mounted() {
        await this.getTour();
        await this.getGuide();
    }
}

</script>

<style scoped>
.form-select{
    background-image: none;
}
</style>
