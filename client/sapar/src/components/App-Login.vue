<template>
    <div class="container-fluid my-5 py-5">
        <div class="container mt-lg-5 mt-4 pt-lg-5 pt-4">
            <form id="login-form" class="text-center mt-3 mx-auto" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Welcome back') }}</h2>
                <div class="input-group mb-3">
                    <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.email" type="email" class="form-control" id="email" name="email" aria-describedby="emailHelp" placeholder="email@example.com">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-eye-slash my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.password" type="password" class="form-control" id="password" name="password" placeholder="**********">
                </div>
                <router-link to="/forgot-password"><p>{{ $t('Forgot password') }}?</p></router-link>
                <button type="submit" class="btn btn-primary my-2 mt-4">Sign in</button> <br/>
                <div class="pb-2"><router-link to="/register"><a>{{ $t('Dont have account? Sign up!') }}</a></router-link></div>
            </form>
            <div class="mt-3 text-center">
            
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

                    var errorMessage = this.$t(error.response.data.detail)
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
                        required: true,
                        pwcheck: true
                    }
                },
                messages: {
                    email: {
                        required: "Email field is required!",
                    },
                    password: {
                        required: "Password field is required",
                        pwcheck: "Invalid Password format"
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
i{
    font-size: 24px;
}
a{
    color: #1C5F41 !important;
    text-decoration: underline !important;
}
</style>