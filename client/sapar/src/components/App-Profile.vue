<template>
    <div id="profile" class="container-fluid mt-5">
        <div class="container">
            <div class="row align-items-center text-center">
                <div class="col-md-5 mx-auto pt-5">
                    <form class="text-center">
                        <h2 class="pt-3">{{ $t('Profile information') }}</h2>
                        <div class="pb-3">
                            <input type="email" v-model="profile.email" class=" form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                            <input type="firstname" v-model="profile.firstName" class="form-control text-center" id="firstname" placeholder="Vasia" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                            <input type="lastname" v-model="profile.lastName" class="form-control text-center" id="lastname" placeholder="Pupkin" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                            <input type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********" :disabled="editMode" :readonly="editMode">
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
        this.$router.push('/login')
      },

      submit() {
        // validate profile and then
        
        let user = this.$store.getters.StateUser;

        this.$store.dispatch("UpdateProfileInfo", {
            id: user.id,
            firstName: this.profile.firstName,
            lastName: this.profile.lastName,
            email: this.profile.email,
        }).then(
            (userData)=> {
                console.log("Profile Update Success!")
                console.log(userData)
                this.changeMode();
            },
            (error)=> {
                console.log("Profile Update Error!")
                console.log(error)
            }
        )
      },

      changeMode() {
		if (this.editMode == null){
            this.editMode = true
        }
        else{
            this.editMode = null
        }
	  }
    },
    mounted() {
        EventBus.on("logout", () => {
            this.logout();
        });

        let user = this.$store.getters.getUser;
        this.$store.dispatch("GetProfileInfo", user.id).then(
            (userData)=> {
                this.profile.firstName = userData.firstName;
                this.profile.lastName = userData.lastName;
                this.profile.email = userData.email;
            },
            (error)=> {
                console.log(`Error: ${error}`)
            }
        );
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
