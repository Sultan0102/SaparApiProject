import { createRouter, createWebHashHistory} from 'vue-router';
import Home from '@/components/App-Home';
import Login from '@/components/App-Login';
import LoginForgotPassword from '@/components/App-LoginForgotPassword';
import LoginEmailCode from '@/components/App-LoginEmailCode';
import Registration from '@/components/App-Registration';
import Profile from '@/components/App-Profile';
import Tickets from '@/components/App-Tickets';
import store from '@/store';


const routes = [
  { 
    path: "/", 
    component: Home, 
    name: "Home"
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
    path: "/email-code", 
    component: LoginEmailCode, 
    name: "LoginEmailCode",
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
  }
]


const vueRouter = createRouter({
  history: createWebHashHistory(),
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
