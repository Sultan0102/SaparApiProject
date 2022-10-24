<template>
    <div class="container-fluid head">
		<div class="container">
			<div class="row align-items-center">
				<div class="col-md-10">
					<ul class="nav">
						<li class="nav-item text-decoration-underline pe-4">
							<router-link to="/" class="nav-link">Main</router-link>
						</li>
							<li class="nav-item">
							<a class="nav-link px-4" href="#">Tickets</a>
						</li>
						<li class="nav-item">
							<a class="nav-link px-4" href="#">Tours</a>
						</li>
						<li class="nav-item">
							<router-link to="/about" class="nav-link px-4">About us</router-link>
						</li>
					</ul>
				</div>
				<div class="col-md-2">
					<div class="nav justify-content-end">
						<span v-if="isLoggedIn">
							<button class="nav-link" @click="logout"><i class="bi bi-box-arrow-left" style="font-size: 4rem; color: white;"></i></button>
						</span>
						<span v-else>
							<router-link to="/login" class="nav-item">Login</router-link> <br>
							<router-link to="/register" class="nav-item">Register</router-link>
						</span>
						
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	computed : {
      isLoggedIn : function(){ return this.$store.getters.isAuthenticated}
    },
	methods: {
      async logout (){
        await this.$store.dispatch('LogOut')
        this.$router.push('/login')
      }
    }
}
</script>
