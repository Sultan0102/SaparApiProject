<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form id="registration-form" class="text-center mt-3" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Welcome') }}</h2>
                <div class="mb-3">
                    <input v-model="form.email" type="email" class="form-control text-center" id="email" name="email" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                    <input v-model="form.firstName" type="firstname" class="form-control text-center" id="firstName" name="firstName" placeholder="Vasia">
                </div>
                <div class="mb-3">
                    <input v-model="form.lastName" type="lastname" class="form-control text-center" id="lastName" name="lastName" placeholder="Pupkin">
                </div>
                <div class="mb-3">
                    <input v-model="form.password" type="password" class="form-control text-center" id="password" name="password" placeholder="**********">
                </div>
                <button type="submit" class="btn btn-primary mb-3">{{ $t('Sign up') }}</button>
            </form>
            <div class="mt-3 text-center">
            <router-link to="/login"><a class="border-bottom">{{ $t('I already have an account') }}</a></router-link>
            </div>
            <div v-if="showError" class="alert alert-danger text-center mt-3" role="alert">
                    <p id="error" class="pt-3">{{ $t('Error during registration') }}</p>
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
                firstName: "",
                lastName: "",
                password: ""
            },
            showError: false
        }
    },
    methods: {
        ...mapActions(["register"]),
        async submit() {
            const user = {
                email: this.form.email,
                password: this.form.password,
                firstName: this.form.firstName,
                lastName: this.form.lastName,
            }
            
            let form = $("#registration-form");


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
            
            this.register(user).then(
                () => {
                    this.$router.push({ name: "VerificationCode", params: { email: this.form.email }})
                    this.$notify({
                        type: 'warn',
                        title: "Verification",
                        text: "Please check your email for a verification code",
                    })
                },
                (error) => {
                    this.showError = true;

                    var errorCode = this.$t(error.response.data.error_code)
                    var errorMessage = this.$t(errorCode)
                    this.$notify({
                        type: 'error',
                        title: "Error",
                        text: errorMessage,
                    })
                }
            )
        },
        enableValidation() {
            let form = $("#registration-form");
            

            form.validate({
                rules: {
                    email: {
                        required: true,
                    },
                    firstName: {
                        required: true,
                    },
                    lastName: {
                        required: true,
                    },
                    password: {
                        required: true,
                        pwcheck: true
                    }
                },
                messages: {
                    password: {
                        pwcheck: "Invalid Password Format!"
                    }
                }
            });
        }
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