import { createRouter, createWebHashHistory} from 'vue-router';
import Home from '@/components/App-Home';
import Login from '@/components/App-Login';
import Registration from '@/components/App-Registration';
import About from '@/components/App-About';
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
    path: "/register", 
    component: Registration, 
    name: "Registration",
    meta: { guest: true },
  },
  { 
    path: "/about", 
    component: About, 
    name: "About",
    meta: { requiresAuth: true },
  },
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
