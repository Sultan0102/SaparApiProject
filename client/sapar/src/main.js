import { createApp } from 'vue'
import App from './App.vue'
import header from '@/components/App-Header'
import footer from '@/components/App-Footer'
import router from '../router/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import config from '../configuration/dev.env'
// temporary global css
import "./assets/css/main.css"
import store from './store/index'

// axios basic configuration
// axios.defaults.withCredentials = true
axios.defaults.baseURL = `${config.BASE_URL}:${config.PORT}/`;


const saparApp = createApp(App);

saparApp.component('App-Header', header);
saparApp.component('App-Footer', footer);

// middleware
saparApp
.use(store)
.use(router)
.use(VueAxios, axios);

saparApp.mount('#app');