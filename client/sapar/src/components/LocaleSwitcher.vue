<template>
    <select class="" v-model="$i18n.locale">
    <option v-for="(locale, i) in locales" :key="`locale-${i}`" :value="locale">
      {{ locale }}
    </option>
    </select>
</template>


<script>

export default {
    name: "LocaleSwitcher",
    data() {
        return { locales: ["ru", "en", "kz"] };
  }
}
</script>

<style scoped>
select{
	color: #FFF !important;
	background-color: #1C5E3C !important;
	border: none !important;
	font-size: 22px !important;
}
</style>
