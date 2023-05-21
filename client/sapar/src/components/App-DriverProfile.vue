<template>
    <div id="profile" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-0 pt-lg-5 pt-0">
            <div class="row align-items-center text-center">
                <div class="col-lg-5 mx-auto pt-5">
                    <form id="edit-profile-form" @submit.prevent="submit">
                        <h2 class="pt-3">{{ $t('Driver Profile information') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                            <input type="email" v-model="driverProfile.email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" placeholder="email@example.com" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" v-model="driverProfile.firstName" id="firstName" name="firstName" class="form-control" placeholder="Vasia" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" v-model="driverProfile.lastName" id="lastName" name="lastName" class="form-control" placeholder="Pupkin" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" v-model="driverProfile.phoneNumber" id="phoneNumber" name="phoneNumber" class="form-control" placeholder="8 707 999 888 777" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="number" v-model="driverProfile.yearExperience" id="yearExperience" name="yearExperience" class="form-control" placeholder="2" :disabled="editMode" :readonly="editMode">
                        </div>

                        <!-- <div class="input-group mb-3">
                            <i class="bi bi-eye-slash my-auto ms-3 ms-sm-5"></i>
                            <input type="password" class="form-control" id="password" name="password" placeholder="**********" :disabled="editMode" :readonly="editMode">
                        </div> -->
                        <button v-if="editMode" @click="changeEditMode()" type="submit" class="btn btn-primary mb-3">{{ $t('Edit') }}</button> 
                        <button v-else type="submit" class="btn btn-primary mb-3">{{ $t('Confirm') }}</button> <br>
                    </form>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import UserService from "@/services/UserService"
import TokenService from "@/services/TokenService"
import useVuelidate from "@vuelidate/core"
import { required } from '@vuelidate/validators';


export default {
    props: ['driverId'],
    setup() {
        return { v$ : useVuelidate() }
    },
    data() {
        return {
            driverProfile: {
                email: null,
                firstName: null,
                lastName: null,
                phoneNumber: null,
                yearExperience: null
            },
            editMode: true
        }
    },
    validations() {
        return {
            driverProfile: {
                email: { required },
                firstName: { required },
                lastName: { required },
                phoneNumber: { required },
                yearExperience: { required }
            }
        }
    },
	methods: {

      async submit() {
        // validate profile and then
        let isValid = await this.v$.$validate();
        if(!isValid) {
            let errorMessages = ''
            this.v$.$errors.forEach((error)=> {
                errorMessages += `Field '${error.$property}'. ${error.$message} </br>`
            })

            this.$notify({
                type: 'error',
                title: 'Validation Error!',
                text: errorMessages
            })
            return;
        }

        const driver = {
            id: this.driverId,
            user: {
                email: this.driverProfile.email,
                firstName: this.driverProfile.firstName,
                lastName: this.driverProfile.lastName,
            },
            yearExperience: this.driverProfile.yearExperience,
            phoneNumber: this.driverProfile.phoneNumber,
        }
        await UserService.updateDriver(driver).then(
            (data)=> {
                UserService.updateLocalUser(data.user);
                this.$store.commit('updateUserFromLocalStorage');
                this.$notify({
                    type: 'success',
                    title: "Update",
                    text: "You've successfully updated driver information!",
                })
            },
            (error)=> {
            var errorCode = this.$t(error.response.data.error_code)
            var errorMessage = this.$t(errorCode)
            this.$notify({
                type: 'error',
                title: "Error",
                text: errorMessage,
            })
        }
        )
      },

      async getDriver() {
        await UserService.retreiveDriverById(this.driverId).then(
            (driver)=> {
            this.driverProfile.email = driver.user.email;
            this.driverProfile.firstName = driver.user.firstName;
            this.driverProfile.lastName = driver.user.lastName; 
            this.driverProfile.phoneNumber = driver.phoneNumber; 
            this.driverProfile.yearExperience = driver.yearExperience; 
        })
      },

      changeEditMode() {
		if (this.editMode == null){
            this.editMode = true
        }
        else{
            this.editMode = null
        }
	  },
    
    },
    async mounted() {
        await this.getDriver();

    },

}
</script>

<style scoped>
p{
    color:#1C5E3C;
    padding-bottom: 0px !important;
}
.order-history{
    border-color: #1C5E3C !important;
	border-top-style: solid;
    border-top-width: 50px;
    background-color: #FFF;

}
.list-group-item{
    border: none !important;
    border-bottom: 1px solid #ECECEC !important;
}
.form-control[readonly]{
    opacity: 0.7 !important;
}
i{
    font-size: 24px;
}
</style>
