<template>
    <select class="" v-model="$i18n.locale" @change="changeLocaleInStore">
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
    },
    methods: {
      changeLocaleInStore() {
        let currentLanguage = this.$i18n.locale;
        this.$store.commit('setCurrentLanguage', currentLanguage)
      }
    },
    mounted() {
      this.$i18n.locale = this.$store.getters.getCurrentLanguage
    }
}
</script>

<style scoped>
select{
	background-color: #1C5E3C !important;
	border: none !important;
	font-size: 22px !important;
}
select, option{
    color: #FFF !important;
}
option{
	background-color: #1C5E3C !important;
}
</style>
