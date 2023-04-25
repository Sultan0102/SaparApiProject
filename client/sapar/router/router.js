import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/App-Home';
import Login from '@/components/App-Login';
import LoginForgotPassword from '@/components/App-LoginForgotPassword';
import VerificationCode from '@/components/VerificationCode';
import PageNotFound from '@/components/PageNotFound';
import PageForbidden from "@/components/PageForbidden"
import PageServerError from "@/components/PageServerError"
import Registration from '@/components/App-Registration';
import RegistrationGuide from '@/components/App-RegistrationGuide';
import RegistrationBusiness from '@/components/App-RegistrationBusiness';
import Profile from '@/components/App-Profile';
import Tickets from '@/components/App-Tickets';
import TourTickets from '@/components/App-TourTickets';
import Order from '@/components/App-Order';
import OrderPassengerInformationList from '@/components/App-OrderPassengerInformationList';
import OrderPayment  from '@/components/App-OrderPayment';
import OrderNumber  from '@/components/App-OrderNumber';
import About from '@/components/App-About';
import GuideApply from '@/components/App-GuideApply';
import GuideVacancyInfo from '@/components/App-GuideVacancyInfo';
import TourInfo from '@/components/App-TourInfo';
import ViewApplications from '@/components/App-ViewApplications';
import GuideInfo from '@/components/App-GuideInfo';
import BusinessProfile from '@/components/App-BusinessProfile';
import BusinessTourList from '@/components/App-BusinessTourList';
import ViewAvailableGuides from '@/components/App-ViewAvailableGuides';
import GuideDeletion from '@/components/App-GuideDeletion';
import Applications from '@/components/App-Applications';
import GuideHire from '@/components/App-GuideHire';
import NewTour from '@/components/App-NewTour';
import AppBusinessToursExample from '@/components/App-BusinessToursExample'
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
    path: "/register-guide", 
    component: RegistrationGuide, 
    name: "RegistrationGuide",
    meta: { guest: true },
  },
  { 
    path: "/register-business", 
    component: RegistrationBusiness, 
    name: "RegistrationBusiness",
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
    props: { scheduleType: 1 }
  },
  { 
    path: "/tour-tickets", 
    component: TourTickets, 
    name: "TourTickets",
    meta: { requiresAuth: true }
  },
  { 
    path: "/order/:id", 
    component: Order, 
    name: "Order",
    meta: { requiresAuth: true },
    props: true,
    // beforeEnter: (to, from) => {
    //   if(from.name != 'Tickets') {
    //     return '/'
    //   }
    // }
  },
  {
    path: "/order/:orderId/passengerInformation", 
    component: OrderPassengerInformationList, 
    name: "OrderPassengerInformation",
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: "/order/:orderId/payment", 
    component: OrderPayment, 
    name: "OrderPayment",
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: "/order/:orderId/number", 
    component: OrderNumber, 
    name: "OrderNumber",
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
  { path: "/:pathMatch(.*)*", 
    component: PageNotFound,
    name: "NotFound" 
  },
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
    path: "/tour-info/:scheduleId", 
    component: TourInfo, 
    name: "TourInfo",
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: "/view-applications", 
    component: ViewApplications, 
    name: "ViewApplications",
    meta: { requiresAuth: true },
  },
  {
    path: "/guide-info", 
    component: GuideInfo, 
    name: "GuideInfo",
    meta: { requiresAuth: true },
  },
  {
    path: "/business-profile", 
    component: BusinessProfile, 
    name: "BusinessProfile",
    meta: { requiresAuth: true },
  },
  {
    path: "/tours", 
    component: BusinessTourList, 
    name: "BusinessTourList",
    meta: { requiresAuth: true },
  },
  {
    path: "/tours-example", 
    component: AppBusinessToursExample, 
    name: "AppBusinessToursExample",
    meta: { requiresAuth: true },
  },
  {
    path: "/view-available-guides", 
    component: ViewAvailableGuides, 
    name: "ViewAvailableGuides",
    meta: { requiresAuth: true },
  },
  {
    path: "/guide-deletion", 
    component: GuideDeletion, 
    name: "GuideDeletion",
    meta: { requiresAuth: true },
  },
  {
    path: "/applications", 
    component: Applications, 
    name: "Applications",
    meta: { requiresAuth: true },
  },
  {
    path: "/guide-hire", 
    component: GuideHire, 
    name: "GuideHire",
    meta: { requiresAuth: true },
  },
  {
    path: "/new-tour", 
    component: NewTour, 
    name: "NewTour",
    meta: { requiresAuth: true },
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
