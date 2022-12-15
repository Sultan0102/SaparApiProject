<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-5" @submit.prevent="submit">
                <h2 class="pt-3">Welcome back</h2>
                <div class="mb-3">
                <input v-model="form.email" type="email" class="form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                <input v-model="form.password" type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********">
                </div>
                <router-link to="/forgot-password"><p>Forgot password?</p></router-link>
                <button type="submit" class="btn btn-primary mb-3">Sign in</button> <br/>
            </form>
            <div class="mt-3 text-center">
            <router-link to="/register"><button type="submit" class="btn btn-primary">Dont have account? Sign up!</button></router-link>
            </div>
            <div v-if="showError" class="alert alert-danger text-center mt-3" role="alert">
                    <p id="error" class="pt-3">Username or Password is incorrect</p>
            </div>
        </div>
    </div>
</template>


<script>
import { mapActions } from "vuex";

export default {
    components: {},
    data() {
        return {
            form: {
                email: "",
                password: "",
            },
            showError: false
        }
    },
    methods: {
        ...mapActions(['LogIn']),
        async submit() {
            const User = new FormData();
            User.append("email", this.form.email);
            User.append("password", this.form.password);
            try {
                await this.LogIn(User);
                console.log("Success action")
                this.$router.push("/home");
                this.showError = false;
            } catch(error) {
                this.showError = true;
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
.alert{
    margin: auto;
    width: 50%;
}
form{
	width: 50%;
}
</style>