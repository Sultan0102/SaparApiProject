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
                            <li v-for="order in slicedOrders"
                            :key="order.id" 
                            class="list-group-item list-group-item-action ps-5"
                            >
                            {{ getFormattedDate(order.schedule.beginDate) }} - {{ getFormattedDate(order.schedule.endDate) }}
                            <br/>
                            {{ getFormattedRoute(order.schedule.route) }}
                            </li>
                            <button type="button" class="btn btn-primary mx-auto mb-3 mt-5" @click="changeOrderVisibility">{{ $t('See more') }}</button>
                        </ul>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import EventBus from "../common/EventBus"
import UserService from "@/services/UserService"
import TokenService from "@/services/TokenService"
import OrderService from "@/services/OrderService"
import RouteService from "@/services/RouteService"


export default {
    data() {
        return {
            profile: {
                email: null,
                firstName: null,
                lastName: null
            },
            editMode: true,
            showMoreOrders: false,
            orders: []
        }
    },
	computed : {
        isLoggedIn : function(){ return this.$store.getters.isAuthenticated },
        slicedOrders: function() {
            let length = this.showMoreOrders 
            ? 3
            : this.orders.length;

            return this.orders.slice(0, length);
        }
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

      changeOrderVisibility() {
        this.showMoreOrders = !this.showMoreOrders;
      },
      
      getFormattedDate(dateStr) {
        let date = new Date(dateStr);
        let currentLanguage = this.$store.getters.getCurrentLanguage;
        let formattedDate = null;
        let formattedTime = null;

        
        switch(currentLanguage) {
            case 'en':
                formattedDate = date.toLocaleDateString('en-UK', { month:"short", day:"numeric", });
                formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute:'2-digit' });
                break;
            case 'ru':
            case 'kz':
                formattedDate = date.toLocaleDateString('ru', { month:"short", day:"numeric", });
                formattedTime = date.toLocaleTimeString('ru', { hour: '2-digit', minute:'2-digit' });
                break;
            default:
                formattedDate = date.toLocaleDateString('en-UK', { month:"short", day:"numeric", });
                formattedTime = date.toLocaleTimeString('en-US', { hour: '2-digit', minute:'2-digit' });
                break;
        }

        return formattedDate + ' ' + formattedTime;
      },

      getFormattedRoute(route) {
        let currentLanguage = 3;

        switch(this.$store.getters.getCurrentLanguage){
            case 'en':
                currentLanguage = 3;
                break;
            case 'ru':
                currentLanguage = 1;
                break;
            case 'kz':
                currentLanguage = 2;
                break;
        }

        let source = route.source.nameCode.codeResourceValues.filter(v => v.language == currentLanguage);
        let destination = route.destination.nameCode.codeResourceValues.filter(v => v.language == currentLanguage);

        if (source.length == 0) {
            source = route.source.nameCode.codeResourceValues[0];
        } else {
            source = source[0];
        }

        if (destination.length == 0) {
            destination = route.destination.nameCode.codeResourceValues[0];
        } else {
            destination = destination[0];
        }

        return source.value + ' - ' + destination.value;
      },

      changeMode() {
		if (this.editMode == null){
            this.editMode = true
        }
        else{
            this.editMode = null
        }
	  },
      async getUserOrders() {
        let orders = []
        await OrderService.getUserOrders(2).then(
            (data)=> {
                orders = data
            },
            (error)=> {
                
            }
        )

        for(let i in orders) {
            await RouteService.retreive(orders[i].schedule.route.id).then(
                (data)=> {
                    orders[i].schedule.route = data
                }
            )
        }

        this.orders = orders;

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
    async mounted() {
        EventBus.on("logout", () => {
            this.logout();
        });

        this.enableValidation();
        const id = TokenService.getUser().id;
        await UserService.retreive(id).then((user)=> {
            this.profile.email = user.email;
            this.profile.firstName = user.firstName;
            this.profile.lastName = user.lastName; 
            UserService.updateLocalUser(this.profile)
            this.$store.commit('updateUserFromLocalStorage');
            
        })
        await this.getUserOrders();
        
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
