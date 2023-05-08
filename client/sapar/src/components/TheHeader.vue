<template>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark">
		<div class="container">
			<router-link to="/home" class="nav-link ms-lg-0 ms-2"><a class="navbar-brand" href="#"><img src="../assets/SAPAR.svg" class="w-75"></a></router-link>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbar">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse row container" id="navbar">
				<ul class="navbar-nav mb-2 mb-lg-0">
					<li class="ms-lg-5">
						<router-link class="nav-link" aria-current="page" to="/tickets">{{ $t('Tickets') }}</router-link>
					</li>
					<li class="ms-lg-5">
						<router-link class="nav-link" aria-current="page" to="/tour-tickets">{{ $t('Tours') }}</router-link>
					</li>
					<li class="ms-lg-5">
						<router-link class="nav-link" aria-current="page" to="/about">{{ $t('About us') }}</router-link>
					</li>
					<li class="ms-lg-5" v-if="getUserRole == 3">
						<router-link class="nav-link" aria-current="page" to="/">{{ $t('Vacancies') }}</router-link>
					</li>
					<li class="ms-lg-auto" v-if="isLoggedIn">
						<router-link class="nav-link" to="/profile">{{ $t('hello') }}, {{ getUserEmail }}<i class="ms-1 bi bi-person-circle"></i></router-link>
					</li>
					<li class="ms-lg-auto" v-else>
						<router-link class="nav-link" to="/register"><span class="border p-1">{{ $t('Sign up') }}</span></router-link>
					</li>
					<li class="my-auto nav-item">
						<LocaleSwitcher class="nav-link" />
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
        },
		getUserRole: function() {
			let user = this.$store.getters.getUser;
			let role = 0
			if (user)
				role = user.role
			return role;
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
i{
	color: #ECECEC;
}
.nav-link:hover{
 opacity: 0.7;
}

</style>