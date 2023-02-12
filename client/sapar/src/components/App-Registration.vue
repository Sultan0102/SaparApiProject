<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-3" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Welcome') }}</h2>
                <div class="mb-3">
                    <input v-model="form.email" type="email" class="form-control text-center" id="exampleInputEmail1" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                    <input v-model="form.firstName" type="firstname" class="form-control text-center" id="firstname" placeholder="Vasia">
                </div>
                <div class="mb-3">
                    <input v-model="form.lastName" type="lastname" class="form-control text-center" id="lastname" placeholder="Pupkin">
                </div>
                <div class="mb-3">
                    <input v-model="form.password" type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********">
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
                password: "",
                username: ""
            },
            showError: false
        }
    },
    methods: {
        ...mapActions(["register"]),
        async submit() {
            const user = {
                email: this.form.email,
                password: this.form.passowrd,
                firstName: this.form.firstName,
                lastName: this.form.lastName,
            }
            this.register(user).then(
                () => {
                    this.$router.push('/home')
                },
                (error) => {
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