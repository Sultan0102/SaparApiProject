<template>
    <div id="profile" class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-0 pt-lg-5 pt-0">
            <div class="row align-items-center text-center">
                <div class="col-lg-5 mx-auto pt-5">
                    <form id="edit-profile-form">
                        <h2 class="pt-3">{{ $t('Profile information') }}</h2>
                        <div class="input-group mb-3 ">
                            <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                            <input type="email" v-model="profile.email" id="email" name="email" class=" form-control" aria-describedby="emailHelp" placeholder="email@example.com" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" v-model="profile.firstName" id="firstName" name="firstName" class="form-control" placeholder="Vasia" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                            <input type="text" v-model="profile.lastName" id="lastName" name="lastName" class="form-control" placeholder="Pupkin" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="input-group mb-3">
                            <i class="bi bi-eye-slash my-auto ms-3 ms-sm-5"></i>
                            <input type="password" class="form-control" id="password" name="password" placeholder="**********" :disabled="editMode" :readonly="editMode">
                        </div>
                        <button v-if="editMode" @click="changeMode()" type="submit" class="btn btn-primary mb-3">{{ $t('Edit') }}</button> 
                        <button v-else @click="submit()" type="submit" class="btn btn-primary mb-3">{{ $t('Confirm') }}</button> <br>
                        <button @click="logout" type="submit" class="btn btn-primary mb-3">{{ $t('Log out') }}</button>
                    </form>
                </div>
                <div class="col-lg-5 mx-auto pt-5">
                    <div class="order-history">
                        <h2 class="my-3">{{ $t('Order History') }}</h2>
                        <ul class="list-group text-start">
                            <li class="list-group-item list-group-item-action ps-5">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</li>
                            <li class="list-group-item list-group-item-action ps-5">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</li>
                            
                            <button type="button" class="btn btn-primary mx-auto mb-3 mt-5">{{ $t('See more') }}</button>
                        </ul>
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
import OrderService from "@/services/OrderService"

export default {
    data() {
        return {
            profile: {
                email: null,
                firstName: null,
                lastName: null
            },
            editMode: true,
            orders: []
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

        OrderService.getUserOrders().then(
            (data)=> {
                this.orders = data
            },
            (error)=> {
                
            }
        )
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
    border-bottom: 1px solid #ECECEC !important;
}
.form-control[readonly]{
    opacity: 0.7 !important;
}
i{
    font-size: 24px;
}
</style>
