<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form id="verification-form" class="text-center mt-5" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Enter the code') }}</h2>    
                <div class="mb-3">
                <input v-model="verificationCode" name="verificationCode" class="form-control form-control-lg text-center" type="text" placeholder="XXXX">
                </div>
                <button type="submit" class="btn btn-primary mb-3">{{ $t('Sign in') }}</button> <br/>
            </form>
            <div v-if="showError" class="alert alert-danger text-center mt-3" role="alert">
                    <p id="error" class="pt-3">{{ $t('Username or Password is incorrect') }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions } from "vuex";
import AuthService from "@/services/AuthService";

export default {
    name: 'VerificationCode',
    props: {
        email: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            verificationCode: ""
        }
    },
    methods: {
        async submit() {
            let form = $("#verification-form");

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
            AuthService.verify(this.email, this.verificationCode).then(()=>{
                this.$router.push({path: "/login"})
                this.$notify({
                    type: 'success',
                    title: "Success",
                    text: "Successfully Verified!",
                })
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
        enableValidation() {
            let form = $("#verification-form");
            
            form.validate({
                rules: {
                    verificationCode: {
                        required: true,
                        digits: true,
                        minlength: 4,
                        maxlength: 4
                    }
                },
                messages: {
                    vefificationCode: {
                        required: "Verification Code field is required",
                        digits: "You can enter only digits!",
                        minlength: "You enter minimum 4 digits",
                        maxlength: "You enter maximum 4 digits",
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

</style>