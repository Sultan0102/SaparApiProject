<template>
    <div class="container-fluid py-5">
        <div class="container">
            <form class="text-center" @submit.prevent="submit">
                <div class="mb-3">
                <h1 class="">Welcome back</h1>
                <input v-model="form.email" type="email" class="form-control text-center" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="email@example.com">
                </div>
                <div class="mb-3">
                <input v-model="form.password" type="password" class="form-control text-center" id="exampleInputPassword1" placeholder="**********">
                </div>
                <button type="submit" class="btn btn-primary mb-3">Sign in</button>
            </form>
            <p v-if="showError" id="error">Username or Password is incorrect</p>
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

