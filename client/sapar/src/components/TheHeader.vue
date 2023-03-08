<template>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark">
		<div class="container">
			<router-link to="/home" class="nav-link "><a class="navbar-brand" href="#"><img src="../assets/SAPAR.svg" class="w-75"></a></router-link>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse row container" id="navbar">
				<ul class="navbar-nav mb-2 mb-lg-0">
					<li class="ms-1 my-auto nav-item">
						<router-link class="nav-link me-2" aria-current="page" to="/tickets">{{ $t('Tickets') }}</router-link>
					</li>
					<li class="ms-1 my-auto nav-item">
						<router-link class="nav-link me-2" aria-current="page" to="/tickets">{{ $t('Tours') }}</router-link>
					</li>
					<li class="ms-1 my-auto nav-item">
						<router-link class="nav-link me-2" aria-current="page" to="/about">{{ $t('About us') }}</router-link>
					</li>
					<li class="ms-1 my-auto nav-item ms-0 ms-lg-auto" v-if="isLoggedIn">
						<router-link class="nav-link d-flex" to="/profile">{{ $t('hello') }} {{ getUserEmail() }}<i class="bi bi-person-circle ms-3 my-auto"></i></router-link>
					</li>
					<li class="my-auto nav-item ms-0 ms-lg-auto" v-else>
						<router-link class="nav-link d-flex" to="/register"><span class="border p-1 me-2">{{ $t('Sign up') }}</span></router-link>
					</li>
					<li class="ms-1 my-auto nav-item my-auto d-flex">
						<LocaleSwitcher class="nav-link " />
					</li>
				</ul>
			</div>
		</div>
	</nav>

</template>

<script>
import { mapGetters } from "vuex";
import LocaleSwitcher from "./LocaleSwitcher.vue";

export default {
    computed: {
        isLoggedIn: function () { return this.$store.getters.isAuthenticated; }
    },
    methods: {
        ...mapGetters(["StateUser"]),
        getUserEmail() {
            let email = this.$store.getters.getUser.email;
            return email;
        }
    },
    components: { LocaleSwitcher }
}
</script>
<style scoped>	
li{
	font-size: 22px;
}

</style>