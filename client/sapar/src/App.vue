<template>
  <div id="app" class="main-container d-flex flex-column h-100 vsc-initialized">
    <TheHeader/>
      <router-view></router-view>
    <TheFooter/>
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>

</style>
