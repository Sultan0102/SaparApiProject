<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-3" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Welcome back') }}</h2>
                <div class="mb-3">
                <input v-model="form.email" type="email" class="form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                <input v-model="form.password" type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********">
                </div>
                <router-link to="/forgot-password"><p>{{ $t('Forgot password') }}?</p></router-link>
                <button type="submit" class="btn btn-primary mb-3">Sign in</button> <br/>
            </form>
            <div class="mt-3 text-center">
            <router-link to="/register"><a class="border-bottom">{{ $t('Dont have account? Sign up!') }}</a></router-link>
            </div>
            <div v-if="showError" class="alert alert-danger text-center mt-3" role="alert">
                    <p id="error" class="pt-3">{{ $t('Username or Password is incorrect') }}</p>
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
        ...mapActions(['login']),
        ...mapActions(['login']),
        async submit() {
            const user = {
                email: this.form.email,
                password: this.form.password
            };
            this.login(user).then(
                ()=> {
                    // success
                    this.showError = false;
                    this.$router.push('/home')    
                },
                (error) => {
                    console.log(error)
                    this.showError = true;
                }
            )
            const user = {
                email: this.form.email,
                password: this.form.password
            };
            this.login(user).then(
                ()=> {
                    // success
                    this.showError = false;
                    this.$router.push('/home')    
                },
                (error) => {
                    console.log(error)
                    this.showError = true;
                }
            )
        }

    }
}
</script>

<style scoped>
p,
a{
    color:#1C5E3C !important;
    padding-bottom: 0px !important;
}
.alert{
    margin: auto;
    width: 50%;
}
form{
	max-width: 600px;
}
</style>