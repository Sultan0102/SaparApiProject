import { createApp } from 'vue'
import App from './App.vue'
import header from '@/components/App-Header'
import footer from '@/components/App-Footer'
import router from '../router/router'
import axious from 'axios'
import VueAxios from 'vue-axios'
// temporary global css
import "./assets/css/main.css"

const saparApp = createApp(App);

saparApp.component('App-Header', header);
saparApp.component('App-Footer', footer);

// middleware
saparApp
.use(router)
.use(VueAxios, axious);

saparApp.mount('#app');