import { createRouter, createWebHashHistory} from 'vue-router';
import Home from '@/components/App-Home'
import Login from '@/components/App-Login'
import Registration from '@/components/App-Registration'


const routes = [
  { path: "/", component: Home, name: "Home" },
  { path: "/home", component: Home, name: "Home" },
  { path: "/login", component: Login, name: "Login" },
  { path: "/register", component: Registration, name: "Registration" },
]


const vueRouter = createRouter({
  history: createWebHashHistory(),
  routes, // routes: routes
})

export default vueRouter;
