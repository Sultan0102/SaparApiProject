<template>
    <div id="profile" class="container-fluid">
        <div class="container">
            <div class="row align-items-center text-center pt-5">
                <div class="col-md-5 mx-auto">
                    <form class="text-center">
                        <h2 class="pt-3">Profile information</h2>
                        <div class="pb-3">
                        <input type="email" class=" form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com" disabled readonly>
                        </div>
                        <div class="pb-3">
                        <input type="username" class="form-control text-center" id="username" aria-describedby="usernameHelp" placeholder="Vasia" disabled readonly>
                        </div>
                        <div class="pb-3">
                        <input type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********" disabled readonly>
                        </div>
                        <button type="submit" class="btn btn-primary mb-3">Edit</button>
                        <button @click="logout" type="submit" class="btn btn-primary mb-3 ms-5">Log out</button>
                    </form>
                </div>
                <div class="col-md-5 mx-auto">
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
	computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated}
    },
	methods: {
      async logout (){
        await this.$store.dispatch('LogOut')
        this.$router.push('/login')
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
</style>
