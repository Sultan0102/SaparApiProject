<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center" @submit.prevent="submit">
                <h1 class="">Welcome back</h1>
                <div class="mb-3">
                <input v-model="form.email" type="email" class="form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                <input v-model="form.username" type="username" class="form-control text-center" id="username" aria-describedby="usernameHelp" placeholder="Vasia">
                </div>
                <div class="mb-3">
                <input v-model="form.password" type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********">
                </div>
                <button type="submit" class="btn btn-primary mb-3">Sign in</button>
            </form>
            <p v-if="showError" id="error">Error during registration</p>
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
                username: "",
                password: "",
            },
            showError: false
        }
    },
    methods: {
        ...mapActions(["Register"]),
        async submit() {
            try {
                await this.Register(this.form);
                this.$router.push("/home");
                this.showError = false;
            } catch(error) {
                this.showError = true;
            }
        }
    }
}

</script>

