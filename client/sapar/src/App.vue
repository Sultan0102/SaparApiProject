<template>
  <div id="app" class="main-container d-flex flex-column h-100 vsc-initialized">
    <TheHeader/>
      <router-view></router-view>
    <TheFooter/>
    <NotificationPopup />
    <notifications position="bottom right" :duration=2500 />
  </div>
</template>

<script>

import NotificationPopup from './components/NotificationPopup.vue';

export default {
  name: 'App',
  components: {
    NotificationPopup
  }
}

</script>

<style>

</style>
