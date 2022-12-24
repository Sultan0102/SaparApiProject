import { createApp } from 'vue'
import App from './App.vue'
import header from '@/components/TheHeader'
import footer from '@/components/TheFooter'
import router from '../router/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import config from '../configuration/dev.env'
// temporary global css
import "./assets/css/main.css"
import store from './store/index'
import setupinterceptors from './services/setupinterceptors'
import Api from "./services/Api"

// axios basic configuration
// axios.defaults.withCredentials = true

// setting up interceptors
[Api.auth, Api.users, Api.tickets].forEach(axiosInstance => setupinterceptors(store, axiosInstance))


const saparApp = createApp(App);

saparApp.component('TheHeader', header);
saparApp.component('TheFooter', footer);

// middleware
saparApp
.use(store)
.use(router)
.use(VueAxios, axios);

saparApp.mount('#app');