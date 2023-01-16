<template>
    <div id="profile" class="container-fluid">
        <div class="container">
            <div class="row align-items-center text-center">
                <div class="col-md-5 mx-auto pt-5">
                    <form class="text-center">
                        <h2 class="pt-3">Profile information</h2>
                        <div class="pb-3">
                        <input type="email" class=" form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                        <input type="firstname" class="form-control text-center" id="firstname" placeholder="Vasia" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                        <input type="lastname" class="form-control text-center" id="lastname" placeholder="Pupkin" :disabled="editMode" :readonly="editMode">
                        </div>
                        <div class="pb-3">
                        <input type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********" :disabled="editMode" :readonly="editMode">
                        </div>
                        <button v-if="editMode" @click="changeMode()" type="submit" class="btn btn-primary mb-3">Edit</button>
                        <button v-else @click="changeMode()" type="submit" class="btn btn-primary mb-3">Submit</button>
                        <button @click="logout" type="submit" class="btn btn-primary mb-3 ms-5">Log out</button>
                    </form>
                </div>
                <div class="col-md-5 mx-auto pt-5">
                    <div class="order-history">
                        <h2 class="mt-2">Order History</h2>
                        <div class="list-group text-center">
                            <div class="list-group-item list-group-item-action">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</div>
                            <div class="list-group-item list-group-item-action">2 Nov 4:00am - 3 Nov 5:30am <br/> Taraz - Almaty</div>
                            
                            <button type="button" class="btn btn-primary mx-auto my-3">See more</button>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</template>


<script>
import store from "@/store/index"

export default {
    data() {
        return {
            editMode: true
        }
    },
	computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated}
    },
	methods: {
      async logout (){
        await this.$store.dispatch('LogOut')
        this.$router.push('/login')
      },
      changeMode() {
		if (this.editMode == null){
            this.editMode = true
        }
        else{
            this.editMode = null
        }
	  }
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
