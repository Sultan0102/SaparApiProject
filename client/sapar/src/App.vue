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

$.validator.addMethod("pwcheck", function(value) {
   let re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!_@#\$%\^&\*])(?=.{8,})");
   
   return re.test(value)
});

$.validator.addMethod("documentNumberFormat", function(value, element, typeElement) {
  let documentFormats = {
    1: '[0-9]{9}',
    2: '^([A-Z]{1})([0-9]{8})'
  }

  const formatId = $(typeElement).val()

  let re = new RegExp(documentFormats[formatId])
  return re.test(value)
})

</script>

<style>

</style>
