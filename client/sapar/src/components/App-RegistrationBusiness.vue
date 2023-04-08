<template>
    <div class="container-fluid my-4 py-4">
        <div class="container mt-lg-5 mt-4 pt-lg-5 pt-4">
            <form id="registration-form" class="text-center mt-3 mx-auto" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Welcome') }}</h2>
                <div class="input-group mb-3">
                    <i class="bi bi-envelope my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.email" type="email" class="form-control" id="email" name="email" placeholder="email@example.com">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.firstName" type="firstname" class="form-control" id="firstName" name="firstName" placeholder="Vasia">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-person-fill my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.lastName" type="lastname" class="form-control" id="lastName" name="lastName" placeholder="Pupkin">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-building my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.companyName" type="companyName" class="form-control" id="companyName" name="companyName" placeholder="Company Name">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-building my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.binNumber" type="binNumber" class="form-control" id="binNumber" name="binNumber" placeholder="BIN Number">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-geo-alt-fill my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.legalAddress" type="legalAddress" class="form-control" id="legalAddress" name="legalAddress" placeholder="Legal Address">
                </div>
                <div class="input-group mb-3">
                    <i class="bi bi-eye-slash my-auto ms-3 ms-sm-5"></i>
                    <input v-model="form.password" type="password" class="form-control" id="password" name="password" placeholder="**********">
                </div>
                <button type="submit" class="btn btn-primary my-2 mt-4">{{ $t('Sign up') }}</button>
                <div class="pb-2"><router-link to="/login"><a>{{ $t('I already have an account') }}</a></router-link></div>
            </form>
            <div class="mt-3 text-center">
            </div>
            <div v-if="showError" class="alert alert-danger text-center mt-3" role="alert">
                    <p id="error" class="pt-3">{{ $t('Error during registration') }}</p>
            </div>
        </div>
    </div>
</template>


<script>
import { mapActions } from "vuex";
import AuthService from "@/services/AuthService";

export default {
    components: {},
    data() {
        return {
            form: {
                email: "",
                firstName: "",
                lastName: "",
                companyName: "",
                binNumber: "",
                legalAddress: "",
                password: ""
            },
            showError: false
        }
    },
    methods: {
        ...mapActions(["register"]),
        async submit() {
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

            const user = {
                email: this.form.email,
                password: this.form.password,
                firstName: this.form.firstName,
                lastName: this.form.lastName,
                companyName: this.form.companyName,
                binNumber: this.form.binNumber,
                legalAddress: this.form.legalAddress,
                roleId: 4
            }
            
            AuthService.registerBusinessPerson(user).then(
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
                    binNumber: {
                        required: true,
                    },
                    companyName: {
                        required: true,
                    },
                    legalAddress: {
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
i{
    font-size: 24px;
}
a{
    color: #1C5F41 !important;
    text-decoration: underline !important;
}
</style>