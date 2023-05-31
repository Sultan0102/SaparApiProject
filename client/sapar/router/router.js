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
import GuideVacancies from '@/components/App-GuideVacancies';
import GuideVacancyInfo from '@/components/App-GuideVacancyInfo';
import TourInfo from '@/components/App-TourInfo';
import ViewApplications from '@/components/App-ViewApplications';
import GuideApply from '@/components/App-GuideApply';
import BusinessTourList from '@/components/App-BusinessTourList';
import ViewAvailableGuides from '@/components/App-ViewAvailableGuides';
import GuideFire from '@/components/App-GuideFire';
import Applications from '@/components/App-Applications';
import GuideHire from '@/components/App-GuideHire';
import DriverProfile from '@/components/App-DriverProfile';
import NewTour from '@/components/App-NewTour';
import AppBusinessToursExample from '@/components/App-BusinessToursExample'
import DriversAdminPanel from '@/components/App-DriversAdminPanel';
import ApplicationsAdminPanel from '@/components/App-ApplicationsAdminPanel';
import RoutesAdminPanel from '@/components/App-RoutesAdminPanel';
import NewRoute from '@/components/App-NewRoute';
import EditRoute from '@/components/App-EditRoute';
import ViewGuideFireApplication from '@/components/App-ViewGuideFireApplication';
import ViewGuideHireApplication from '@/components/App-ViewGuideHireApplication';
import ViewNewRouteApplication from '@/components/App-ViewNewRouteApplication';
import ViewSabbaticalApplication from '@/components/App-ViewSabbaticalApplication';
import ViewRemoveRouteApplication from '@/components/App-ViewRemoveRouteApplication';
import ViewSickLeaveApplication from '@/components/App-ViewSickLeaveApplication';
import store from '@/store';
import TokenService from '@/services/TokenService';


const routes = [
  { 
    path: "/", 
    redirect: '/home',
    meta: { 
      isForEveryone: true
    }
  }, 
  { 
    path: "", 
    redirect: '/home',
    meta: { 
      isForEveryone: true
    }
  }, 
  { 
    path: "/home", 
    component: Home, 
    name: "Home",
    meta: { 
      isForEveryone: true
    }
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
    meta: { 
      isForEveryone: true
    }
  },
  { 
    path: "/tickets", 
    component: Tickets, 
    name: "Tickets",
    meta: { requiresAuth: true, isForEveryone: true },
    props: { scheduleType: 1 }
  },
  { 
    path: "/tour-tickets", 
    component: TourTickets, 
    name: "TourTickets",
    meta: { requiresAuth: true, isForEveryone: true }
  },
  { 
    path: "/order/:id", 
    component: Order, 
    name: "Order",
    meta: { requiresAuth: true, isForEveryone: true },
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
    meta: { requiresAuth: true, isForEveryone: true },
    props: true
  },
  {
    path: "/order/:orderId/payment", 
    component: OrderPayment, 
    name: "OrderPayment",
    meta: { requiresAuth: true, isForEveryone: true },
    props: true
  },
  {
    path: "/order/:orderId/number", 
    component: OrderNumber, 
    name: "OrderNumber",
    meta: { requiresAuth: true, isForEveryone: true },
  },
  {
    path: "/about", 
    component: About, 
    name: "About",
    meta: {
      isForEveryone: true
    }
  },
  {
    path: "/vacancies", 
    component: GuideVacancies, 
    name: "GuideVacancies",
    meta: { requiresAuth: true, isForGuide: true },
  },
  {
    path: "/guide-vacancy-info", 
    component: GuideVacancyInfo, 
    name: "GuideVacancyInfo",
    meta: { requiresAuth: true },
  },
  { path: "/:pathMatch(.*)*", 
    component: PageNotFound,
    name: "NotFound",
    meta: {
      isForEveryone: true
    }
  },
  {
    path: "/forbidden", 
    component: PageForbidden, 
    name: "Forbidden",
    meta: {
      isForEveryone: true
    }
  },
  {
    path: "/serverError", 
    component: PageServerError, 
    name: "PageServerError",
    meta: {
      isForEveryone: true
    }
  },
  {
    path: "/tour-info/:scheduleId", 
    component: TourInfo, 
    name: "TourInfo",
    meta: { requiresAuth: true, isForEveryone: true },
    props: true
  },
  {
    path: "/view-applications", 
    component: ViewApplications, 
    name: "ViewApplications",
    meta: { requiresAuth: true, isForAdmin: true },
  },
  {
    path: "/vacancies/apply/tour/:tourId", 
    component: GuideApply, 
    name: "GuideApply",
    meta: { requiresAuth: true, isForGuide: true },
    props: true,
  },
  {
    path: "/tours", 
    component: BusinessTourList, 
    name: "BusinessTourList",
    meta: { requiresAuth: true, isForBusinessPerson: true },
  },
  {
    path: "/tours-example", 
    component: AppBusinessToursExample, 
    name: "AppBusinessToursExample",
    meta: { requiresAuth: true, isForEveryone: true },
  },
  {
    path: "/tour/:tourId/available-guides", 
    component: ViewAvailableGuides, 
    name: "ViewAvailableGuides",
    meta: { requiresAuth: true, isForBusinessPerson: true },
    props: true
  },
  {
    path: "/tour/:tourId/guide-fire/:guideId", 
    component: GuideFire, 
    name: "GuideFire",
    meta: { requiresAuth: true, isForBusinessPerson: true },
    props: true
  },
  {
    path: "/profile/applications", 
    component: Applications, 
    name: "ProfileApplications",
    meta: { requiresAuth: true, isForBusinessPerson: true, isForGuide: true }
  },
  {
    path: "/profile/applications/:applicationId/fire", 
    component: ViewGuideFireApplication, 
    name: "ViewGuideFireApplication",
    meta: { requiresAuth: true, isForBusinessPerson: true, isForGuide: true },
    props: true
  },
  {
    path: "/profile/applications/:applicationId/hire", 
    component: ViewGuideHireApplication, 
    name: "ViewGuideHireApplication",
    meta: { requiresAuth: true, isForBusinessPerson: true, isForGuide: true },
    props: true
  },
  {
    path: "/drivers-admin-panel/applications/newRoute/:applicationId", 
    component: ViewNewRouteApplication, 
    name: "ViewNewRouteApplication",
    meta: { requiresAuth: true, isForAdmin: true },
    props: true
  },
  {
    path: "/drivers-admin-panel/applications/sabbatical/:applicationId", 
    component: ViewSabbaticalApplication, 
    name: "ViewSabbaticalApplication",
    meta: { requiresAuth: true, isForAdmin: true },
    props: true
  },
  {
    path: "/drivers-admin-panel/applications/removeRoute/:applicationId", 
    component: ViewRemoveRouteApplication, 
    name: "ViewRemoveRouteApplication",
    meta: { requiresAuth: true, isForAdmin: true },
    props: true
  },
  {
    path: "/drivers-admin-panel/applications/sickLeave/:applicationId", 
    component: ViewSickLeaveApplication, 
    name: "ViewSickLeaveApplication",
    meta: { requiresAuth: true, isForAdmin: true },
    props: true
  },
  {
    path: "/tour/:tourId/guide-hire/:guideId", 
    component: GuideHire, 
    name: "GuideHire",
    meta: { requiresAuth: true, isForBusinessPerson: true },
    props: true
  },
  {
    path: "/new-tour", 
    component: NewTour, 
    name: "NewTour",
    meta: { requiresAuth: true, isForBusinessPerson: true },
  },
  // Admin Panel Components
  {
    path: "/driver/:driverId",
    component: DriverProfile,
    name: "DriverProfile",
    meta: { requiresAuth: true, isForAdmin: true },
    props: true
  },
  {
    path: "/drivers-admin-panel", 
    component: DriversAdminPanel, 
    name: "DriversAdminPanel",
    meta: { 
      requiresAuth: true,
      isForAdmin: true
    },
  },
  {
    path: "/applications-admin-panel", 
    component: ApplicationsAdminPanel, 
    name: "ApplicationsAdminPanel",
    meta: { 
      requiresAuth: true,
      isForAdmin: true
    },
  },
  {
    path: "/routes-admin-panel", 
    component: RoutesAdminPanel, 
    name: "RoutesAdminPanel",
    meta: { requiresAuth: true, isForAdmin: true },
  },
  {
    path: "/new-route", 
    component: NewRoute, 
    name: "NewRoute",
    meta: { requiresAuth: true, isForAdmin: true },
  },
  {
    path: "/edit-route", 
    component: EditRoute, 
    name: "EditRoute",
    meta: { requiresAuth: true, isForAdmin: true },
  }
]


const vueRouter = createRouter({
  history: createWebHistory(),
  routes,
})


// control access to pages
vueRouter.beforeEach((to, from, next) => {
  const user = TokenService.getUser();
  if(store.getters.isAuthenticated) {
    if(user.role == 1 && to.matched.every(record => record.meta.isForAdmin || record.meta.isForEveryone)) {
      next();
    } else if(user.role == 2 && to.matched.every(record => record.meta.isForEveryone)) {
      next();
    } else if(user.role == 3 && to.matched.every(record => record.meta.isForGuide || record.meta.isForEveryone)) {
      next();
    } else if(user.role == 4 && to.matched.every(record => record.meta.isForBusinessPerson || record.meta.isForEveryone)) {
      next();
    }
    else {
      next('/forbidden')
    }
  } else {
    next();
  }

});

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
