<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center mt-5" @submit.prevent="submit">
                <h2 class="pt-3">{{ $t('Enter the code') }}</h2>    
                <div class="mb-3">
                <input v-model="verificationCode" class="form-control form-control-lg text-center" type="text" placeholder="XXXX">
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

export default {
    components: {},
    props:['email'],
    data() {
        return {
            verificationCode: "",
            showError: false
        }
    },
    methods: {
        async submit() {
            console.log(this.email)
            console.log(this.verificationCode)
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
	max-width: 600px;
}
</style>