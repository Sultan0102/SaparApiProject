<template>
    <div id="profile" class="container-fluid mt-5">
        <div class="container">
            <div class="row align-items-center text-center">
                <div class="col-md-5 mx-auto pt-5">
                    <form id="edit-profile-form" class="text-center">
                        <h2 class="pt-3">{{ $t('Profile information') }}</h2>
                        <div class="pb-3">
                            <input type="email" v-model="profile.email" id="email" name="email" class=" form-control text-center" aria-describedby="emailHelp" placeholder="email@example.com" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                            <input type="text" v-model="profile.firstName" id="firstName" name="firstName" class="form-control text-center" placeholder="Vasia" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                            <input type="text" v-model="profile.lastName" id="lastName" name="lastName" class="form-control text-center" placeholder="Pupkin" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                            <input type="password" class="form-control text-center" id="password" name="password" placeholder="**********" :disabled="editMode" :readonly="editMode">
                        </div>
                        <button v-if="editMode" @click="changeMode()" type="submit" class="btn btn-primary mb-3">{{ $t('Edit') }}</button>
                        <button v-else @click="submit()" type="submit" class="btn btn-primary mb-3">{{ $t('Confirm') }}</button>
                        <button @click="logout" type="submit" class="btn btn-primary mb-3 ms-5">{{ $t('Log out') }}</button>
                    </form>
                </div>
                <div class="col-md-5 mx-auto pt-5">
                    <div class="order-history">
                        <h2 class="mt-2">{{ $t('Order History') }}</h2>
                        <div class="list-group text-center">
                            <div class="list-group-item list-group-item-action">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</div>
                            <div class="list-group-item list-group-item-action">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</div>
                            
                            <button type="button" class="btn btn-primary mx-auto my-3">{{ $t('See more') }}</button>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
//import { isEmptyStatement } from '@babel/types'
import EventBus from "../common/EventBus"
import UserService from "@/services/UserService"
import TokenService from "@/services/TokenService"

export default {
    data() {
        return {
            profile: {
                email: null,
                firstName: null,
                lastName: null
            },
            editMode: true
        }
    },
	computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated}
    },
	methods: {
      logout() {
        this.$store.dispatch('logout')
        this.$router.push('/home')
      },

      submit() {
        // validate profile and then
        let form = $("#edit-profile-form")

        if(!form.valid()) {
            var validateResult = form.validate();
            var errorMessages = '';

            validateResult.errorList.forEach(function (error) {
                errorMessages += error.message + '<br />';
            });
            this.$notify({
                type: 'error',
                text: errorMessages
            })
            return;
        }
        debugger;
        const id = TokenService.getUser().id;
        const user = {
            id,
            email: this.profile.email,
            firstName: this.profile.firstName,
            lastName: this.profile.lastName,
        }

        UserService.update(user).then(()=> {
            UserService.updateLocalUser();
            this.$store.commit('updateUserFromLocalStorage');
        }, 
        (error)=> {
            var errorCode = this.$t(error.response.data.error_code)
            var errorMessage = this.$t(errorCode)
            this.$notify({
                type: 'error',
                title: "Error",
                text: errorMessage,
            })
        })
        
      },

      changeMode() {
		if (this.editMode == null){
            this.editMode = true
        }
        else{
            this.editMode = null
        }
	  },
      enableValidation() {
        let form = $("#edit-profile-form");
        form.validate({
            rules: {
                email: {
                    required: true
                },
                firstName: {
                    required: true
                }, 
                lastName: {
                    required: true
                }
            },
        });
    }
    },
    mounted() {
        EventBus.on("logout", () => {
            this.logout();
        });

        this.enableValidation();
        const id = TokenService.getUser().id;
        UserService.retreive(id).then((user)=> {
            this.profile.email = user.email;
            this.profile.firstName = user.firstName;
            this.profile.lastName = user.lastName; 
            UserService.updateLocalUser(this.profile)
            this.$store.commit('updateUserFromLocalStorage');
            
        })
    },
    beforeMount() {
        EventBus.remove("logout");
    }
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
}
.form-control[readonly]{
    opacity: 0.7 !important;
}
</style>
