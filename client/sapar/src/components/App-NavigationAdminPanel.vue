<template> 
    <div class="col-xl-3">
        <router-link class="nav-link" to="/drivers-admin-panel"><button class="btn btn-primary my-4 ms-xl-0 ms-5">{{ $t('Drivers') }}</button></router-link>
        <router-link class="nav-link" to="/routes-admin-panel"><button class="btn btn-primary my-4 ms-xl-0 ms-5">{{ $t('Routes') }}</button></router-link>
        <router-link class="nav-link" to="/routes-admin-panel"><button class="btn btn-primary my-4 ms-xl-0 ms-5">{{ $t('Tours') }}</button></router-link>
        <router-link class="nav-link" to="/applications-admin-panel"><button class="btn btn-primary my-4 ms-xl-0 ms-5">{{ $t('Applications') }}</button></router-link>
    </div>
</template>