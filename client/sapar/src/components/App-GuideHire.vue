<template>
    <div class="container-fluid my-4 py-4" v-if="tour && guide">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto" @submit.prevent="sendApplication">
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
                                <!-- <VueDatePicker v-model="application.effectiveFromDate"
                                model-auto
                                position="left" 
                                placeholder="Effective from" 
                                hide-input-icon 
                                /> -->
                                <VueDatePicker v-model="application.effectiveFromDate"
                                hide-input-icon
                                placeholder="Effective from"
                                position="left"
                                :enable-time-picker="false"
                                ignore-time-validation
                                :allowed-dates="allowedDates"
                                :start-date="nearestAllowedDate"
                                />
                                
                                
                            </div>
                        </div>
                        
                        <div class="input-group mb-3">
                            <i class="bi bi-clock ms-4 ms-sm-5 my-auto"></i>
                            <input type="text" class="form-control" readonly :value="tourTime"/>
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
    import TokenService from '@/services/TokenService';
    import ApplicationService from "@/services/ApplicationService"
    import useVuelidate from '@vuelidate/core';
    import { required } from '@vuelidate/validators';


    export default {
        props: ['tourId', 'guideId'],
        setup() {
            return { v$: useVuelidate() }
        },
        validations() {
            return {
                application: {
                    email: { required },
                    firstName: { required },
                    lastName: { required },
                    effectiveFromDate: { required }
                },
            }
        },
        data() {
            return {
                myDate: null,
                tour: null,
                guide: null,
                application: {
                    email: null,
                    firstName: null,
                    lastName: null,
                    effectiveFromDate: null,
                },
            }
        },
        computed: {
            allowedDates: function() {
                console.log(this.tour.schedules)
                let schedules = this.tour.schedules.filter(s => new Date(s.beginDate) > new Date())
                return schedules.map(s => new Date(s.beginDate))
            },
            nearestAllowedDate: function() {
                return this.allowedDates[0];
            },
            tourTime: function() {
                let schedule = this.tour.schedules[0]
                let beginTime = new Date(schedule.beginDate).toLocaleTimeString('ru')
                let endTime = new Date(schedule.endDate).toLocaleTimeString('ru')

                return beginTime + " " + endTime
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
            formatDate: (date)=> {
                const day = date.getDate();
                const month = date.getMonth() + 1;
                const year = date.getFullYear();

                return `Selected date is ${day}/${month}/${year}`;
            },
            async sendApplication() {
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
                const applicationData = {
                    guide: this.guideId,
                    email: this.application.email,
                    firstName: this.application.firstName,
                    lastName: this.application.lastName,
                    effectiveFrom: this.application.effectiveFromDate.toISOString(),
                    tour: this.tourId
                }

                const applicationRequest = {
                    senderUser: TokenService.getUser().id,
                    receiverUser: this.guide.user.id,
                    status: 1,
                    type: 1,
                    applicationData: applicationData,
                    documents: []
                }

                await ApplicationService.createApplication(applicationRequest).then(
                    (data)=> {
                        this.$router.push( {name: "Profile"} )
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
            console.log(this.tour)
            console.log(this.guide)
        }
    }

</script>

<style scoped>
.form-select{
    background-image: none;
}
</style>
