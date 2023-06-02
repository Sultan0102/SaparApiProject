<template>
    <div v-if="application && driver" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-3 pt-lg-5 pt-3">
            <div class="row align-items-center text-center">
                <div class="mx-auto pt-5">
                    <form class="mx-auto" @submit.prevent="false">
                        <h2 class="pt-3">{{ $t('Remove Route Application') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-4 ms-sm-5"></i>
                            <input :value="driver.user.email" type="email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input :value="driver.user.firstName" type="text" id="firstName" name="firstName" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-4 ms-sm-5"></i>
                            <input :value="driver.user.lastName" type="text" id="lastName" name="lastName" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-justify my-auto ms-4 ms-sm-5"></i>
                            <input :value="schedule.scheduleNumber" type="text" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-map my-auto ms-4 ms-sm-5"></i>
                            <input :value="schedule.route.sourceName" type="text" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-map my-auto ms-4 ms-sm-5"></i>
                            <input :value="schedule.route.destinationName" type="text" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-calendar my-auto ms-4 ms-sm-5"></i>
                            <input :value="getFormattedDateTime(schedule.beginDate)" type="text" class="form-control" readonly disabled>
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-calendar my-auto ms-4 ms-sm-5"></i>
                            <input :value="getFormattedDateTime(schedule.endDate)" type="text" class="form-control" readonly disabled>
                        </div>
                        <button type="submit" class="btn btn-primary mt-5 mb-3" @click="approveApplication">{{ $t('Approve') }}</button> <br/>
                        <button type="submit" class="btn btn-primary mb-3" @click="declineApplication">{{ $t('Decline') }}</button> <br/>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import ApplicationService from '@/services/ApplicationService';
import ScheduleService from '@/services/ScheduleService';
import UserService from '@/services/UserService';


export default {
    props: ['applicationId'],
    data() {
        return {
            application: null,
            driver: null,
            schedule: null
        }
    }, 

    methods: {

        getFormattedDateTime(dateTimeIsoStr) {
            let dateTime = new Date(dateTimeIsoStr);

            let day = dateTime.getDay()
            let month = dateTime.getMonth()
            
            if (day < 10) day = '0'+day
            if (month < 10) month = '0'+month
            
            if (dateTime == null) return '';

            return `${day}.${month}.${dateTime.getFullYear()}`
        },

        async getApplication() {
            await ApplicationService.retreive(this.applicationId).then(
                (data) => {
                    this.application = data
                    console.log(this.application);

                    this.getDriver(this.application.senderUser);
                    this.getSchedule(this.application.applicationData['Schedule id'])
                }
            )

        },

        async getSchedule(scheduleId) {
            await ScheduleService.retreive(scheduleId).then(
                (data)=> {
                    this.schedule = data;
                }
            )
        },

        async getDriver(userId) {
            await UserService.retreiveDriverByUserId(userId).then(
                (data) => {
                    this.driver = data
                }
            )
        },

        async approveApplication() {
            const criteria = {
                applicationId: this.application.id,
                status: 2
            }
            await ApplicationService.updateApplicationStatus(criteria).then(
                (data)=> {
                    this.$router.push({ name: 'DriversAdminPanel'})
                    this.$notify({
                        type: 'success',
                        title: 'Application',
                        text: "Application was successfull approved!"
                    })

                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: 'Application',
                        text: "Error updating application status"
                    })
                }
            )
        },

        async declineApplication() {
            const criteria = {
                applicationId: this.application.id,
                status: 3
            }
            await ApplicationService.updateApplicationStatus(criteria).then(
                (data)=> {
                    this.$router.push({ name: 'DriversAdminPanel'})
                    this.$notify({
                        type: 'success',
                        title: 'Application',
                        text: "Application was successfull declined"
                    })
                },
                (error)=> {
                    this.$notify({
                        type: 'error',
                        title: 'Application',
                        text: "Error updating application status"
                    })
                }
            )
        }

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
