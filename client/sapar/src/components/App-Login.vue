<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form id="login-form" class="text-center mt-3" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Welcome back') }}</h2>
                <div class="mb-3">
                <input v-model="form.email" type="email" class="form-control text-center" id="email" name="email" aria-describedby="emailHelp" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                <input v-model="form.password" type="password" class="form-control text-center" id="password" name="password" placeholder="**********">
                </div>
                <router-link to="/forgot-password"><p>{{ $t('Forgot password') }}?</p></router-link>
                <button type="submit" class="btn btn-primary mb-3">Sign in</button> <br/>
            </form>
            <div class="mt-3 text-center">
            <router-link to="/register"><a class="border-bottom">{{ $t('Dont have account? Sign up!') }}</a></router-link>
            </div>
            <div v-if="showError" class="alert alert-danger text-center mt-3" role="alert">
                    <p id="error" class="pt-3">{{ $t('Username or Password is incorrect') }}</p>
                    <p id="error2" class="pt-3">{{ errorMessage }}</p>
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
            showError: false,
            errorMessage: ''
        }
    },
    methods: {
        ...mapActions(['login']),
        async submit() {
            const user = {
                email: this.form.email,
                password: this.form.password
            };
            var form = $("#login-form");
            
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

            this.login(user).then(
                ()=> {
                    this.showError = false;
                     
                    this.$router.push("/")
                },
                (error) => {

                    if(error.response.data.error_code == 'user_not_verified') {
                        this.$router.push({ name: "VerificationCode", params: { email: this.form.email }})      
                    }

                    var errorCode = this.$t(error.response.data.error_code)
                    var errorMessage = this.$t(errorCode)
                    this.$notify({
                        type: 'error',
                        title: "Error",
                        text: errorMessage,
                    })
                    
                    
                    
                    this.showError = true;
                }
            )
        },
        enableValidation() {
            var loginForm = $("#login-form");
            loginForm.validate({
                rules: {
                    email: {
                        required: true
                    },
                    password: {
                        required: true
                    }
                },
                messages: {
                    email: {
                        required: "Email field is required!",
                    },
                    password: {
                        required: "Password field is required"
                    }
                }
            })
        },
        
    },
    mounted() {
        this.enableValidation();
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