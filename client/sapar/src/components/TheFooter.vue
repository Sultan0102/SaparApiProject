<template>
<footer class="footer mt-auto">
	<div class="container-fluid">
		<div class="container">
			<div class="row align-items-center text-center">
				<div class="col-lg-3">
					<ul class="nav">
						<li class="nav-item center-item">
							<a class="nav-link" href="#"><i class="bi bi-telegram"></i></a>
						</li>
							<li class="nav-item center-item">
							<a class="nav-link" href="#"><i class="bi bi-instagram"></i></a>
						</li>
						<li class="nav-item center-item">
							<a class="nav-link" href="#"><i class="bi bi-whatsapp"></i></a>
						</li>
					</ul>

				</div>
				<div class="col-lg-6">
					<div class="row align-items-center text-center">
						<div class="col-4"><hr></div>
						<div class="col-4"><router-link to="/home" class="nav-link"><a class="navbar-brand" href="#"><img src="../assets/SAPAR.svg" class="img-fluid"></a></router-link></div>
						<div class="col-4"><hr></div>
					</div>

				</div>
				<div class="col-lg-3">
					<ul class="nav">
						<li class="nav-item center-item">
							<a class="nav-link" href="#"><i class="bi bi-twitter"></i></a>
						</li>
							<li class="nav-item center-item">
							<a class="nav-link" href="#"><i class="bi bi-linkedin"></i></a>
						</li>
						<li class="nav-item center-item">
							<a class="nav-link" href="#"><i class="bi bi-google"></i></a>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
	</footer>
</template>

<script>
</script>

<style scoped>
i{
	color: #ECECEC;
}
hr{
    border: 1px solid #ECECEC !important;
    opacity: 0.5;
}
</style>