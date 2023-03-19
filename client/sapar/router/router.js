import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import Home from '@/components/App-Home';
import Login from '@/components/App-Login';
import LoginForgotPassword from '@/components/App-LoginForgotPassword';
import VerificationCode from '@/components/VerificationCode';
import PageNotFound from '@/components/PageNotFound';
import PageForbidden from "@/components/PageForbidden"
import PageServerError from "@/components/PageServerError"
import Registration from '@/components/App-Registration';
import Profile from '@/components/App-Profile';
import Tickets from '@/components/App-Tickets';
import Tickets2 from '@/components/App-Tickets2';
import Order from '@/components/App-Order';
import OrderPassengerInformation from '@/components/App-OrderPassengerInformation';
import OrderPayment  from '@/components/App-OrderPayment';
import About from '@/components/App-About';
import GuideApply from '@/components/App-GuideApply';
import GuideVacancyInfo from '@/components/App-GuideVacancyInfo';
import Error403 from '@/components/App-Error403';
import Error404 from '@/components/App-Error404';
import Error500 from '@/components/App-Error500';
import store from '@/store';


const routes = [
  { 
    path: "/", 
    redirect: '/home'
  }, 
  { 
    path: "", 
    redirect: '/home'
  }, 
  { 
    path: "/home", 
    component: Home, 
    name: "Home" 
  },
  { 
    path: "/login", 
    component: Login, 
    name: "Login",
    meta: { guest: true },
  },
  { 
    path: "/forgot-password", 
    component: LoginForgotPassword, 
    name: "LoginForgotPassword",
    meta: { guest: true },
  },
  { 
    path: "/email-code/:email", 
    component: VerificationCode, 
    name: "VerificationCode",
    props: true,
    meta: { guest: true },
  },
  { 
    path: "/register", 
    component: Registration, 
    name: "Registration",
    meta: { guest: true },
  },
  { 
    path: "/profile", 
    component: Profile, 
    name: "Profile",
    meta: { requiresAuth: true },
  },
  { 
    path: "/tickets", 
    component: Tickets, 
    name: "Tickets",
    meta: { requiresAuth: true },
  },
  { 
    path: "/tickets2", 
    component: Tickets2, 
    name: "Tickets2",
    meta: { requiresAuth: true },
  },
  { 
    path: "/order", 
    component: Order, 
    name: "Order",
    meta: { requiresAuth: true },
  },
  {
    path: "/order-passenger-information", 
    component: OrderPassengerInformation, 
    name: "OrderPassengerInformation",
    meta: { requiresAuth: true },
  },
  {
    path: "/order-payment", 
    component: OrderPayment, 
    name: "OrderPayment",
    meta: { requiresAuth: true },
  },
  {
    path: "/about", 
    component: About, 
    name: "About"
  },
  {
    path: "/guide-apply", 
    component: GuideApply, 
    name: "GuideApply",
    meta: { requiresAuth: true },
  },
  {
    path: "/guide-vacancy-info", 
    component: GuideVacancyInfo, 
    name: "GuideVacancyInfo",
    meta: { requiresAuth: true },
  },
  { path: "/:pathMatch(.*)*", component: PageNotFound },
  {
    path: "/forbidden", 
    component: PageForbidden, 
    name: "Forbidden"
  },
  {
    path: "/serverError", 
    component: PageServerError, 
    name: "PageServerError"
  },
  {
    path: "/error403", 
    component: Error403, 
    name: "Error403"
  },
  {
    path: "/error404", 
    component: Error404, 
    name: "Error404"
  },
  {
    path: "/error500", 
    component: Error500, 
    name: "Error500"
  }
]


const vueRouter = createRouter({
  history: createWebHistory(),
  routes,
})


// do not let unauthorized users access auth pages
vueRouter.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if(store.getters.isAuthenticated) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }

});

// stop authenticated users from accessing 'guest' pages
vueRouter.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next("/home");
      return;
    }
    next();
  } else {
    next();
  }
});




export default vueRouter;
