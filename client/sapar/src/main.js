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
import i18n from './i18n'
import Notifications from '@kyvg/vue3-notification'

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

// axios basic configuration
// axios.defaults.withCredentials = true

// setting up interceptors
[Api.auth, 
Api.users, 
Api.tickets, 
Api.schedules, 
Api.orders, 
Api.cachedTicketPersons, 
Api.ticketPersons, 
Api.passportTypes, 
Api.payments, 
Api.routes,
Api.tours].forEach(axiosInstance => setupinterceptors(store, router, axiosInstance))


const saparApp = createApp(App);

saparApp.component('TheHeader', header);
saparApp.component('TheFooter', footer);
saparApp.component('VueDatePicker', VueDatePicker);

// middleware
saparApp
.use(i18n)
.use(store)
.use(router)
.use(VueAxios, axios)
.use(Notifications);

saparApp.mount('#app');