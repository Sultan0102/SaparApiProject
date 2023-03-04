<template>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark">
		<div class="container">
			<router-link to="/home" class="nav-link "><a class="navbar-brand" href="#"><img src="../assets/SAPAR.svg" class="w-75"></a></router-link>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse row container" id="navbar">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0 col-6">
					<li class="nav-item">
						<router-link class="nav-link me-2" aria-current="page" to="/tickets">{{ $t('Tickets') }}</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link me-2" aria-current="page" to="/tickets">{{ $t('Tours') }}</router-link>
					</li>
					<li class="nav-item">
						<router-link class="nav-link me-2" aria-current="page" to="/about">{{ $t('About us') }}</router-link>
					</li>
				</ul>
				<ul class="navbar-nav justify-content-end mb-2 mb-lg-0 col-6">
					<li class="nav-item" v-if="isLoggedIn">
						<router-link class="nav-link d-flex justify-content-end" to="/profile">{{ $t('hello') }} {{ getUserEmail }}<i class="bi bi-person-circle ms-3"></i></router-link>
					</li>
					<li class="nav-item" v-else>
						<router-link class="nav-link d-flex justify-content-end" to="/register"><span class="border p-1 me-2">{{ $t('Sign up') }}</span></router-link>
					</li>
					<li class="nav-item my-auto d-flex justify-content-end">
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
        isLoggedIn: function () { return this.$store.getters.isAuthenticated; },
		getUserEmail: function() {
            let email = this.$store.getters.getUser.email;
            return email;
        }
    },
    methods: {
        
    },
    components: { LocaleSwitcher }
}
</script>
<style scoped>	
li{
	font-size: 22px;
}

</style>