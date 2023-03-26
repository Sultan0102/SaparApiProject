<template>

<div class="container-fluid py-5 mt-5">
  <div class="container">
    <VueDatePicker v-model="date" model-auto range position="left"/>
    <p v-if="date">Selected date: {{ date }}</p>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue';

const date = ref();
</script>

