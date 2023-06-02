import axios from 'axios'
import config from '../../configuration/dev.env'
import store from '@/store/index'


export default {
    auth: axios.create({
        baseURL: config.AUTH_API_URL,
    }),
    users: axios.create({
        baseURL: config.USERS_API_URL,
    }),
    tickets: axios.create({
        baseURL: config.TICKETS_API_URL,
    }),
    schedules: axios.create({
        baseURL: config.SCHEDULES_API_URL,
    }),
    ticketPersons: axios.create({
        baseURL: config.TICKET_PERSONS_API_URL,
    }),
    cachedTicketPersons: axios.create({
        baseURL: config.CACHED_TICKET_PERSONS_API_URL,
    }),
    orders: axios.create({
        baseURL: config.ORDERS_API_URL,
    }),
    passportTypes: axios.create({
        baseURL: config.PASSPORT_TYPES_API_URL,
    }),
    payments: axios.create({
        baseURL: config.PAYMENTS_API_URL,
    }),
    routes: axios.create({
        baseURL: config.ROUTES_API_URL,
    }),
    tours: axios.create({
        baseURL: config.TOURS_API_URL,
    }),
    guides: axios.create({
        baseURL: config.GUIDES_API_URL,
    }),
    applications: axios.create({
        baseURL: config.APPLICATIONS_API_URL,
    }),
    documents: axios.create({
        baseURL: config.DOCUMENTS_API_URL,
    }),
    drivers: axios.create({
        baseURL: config.DRIVERS_API_URL,
    }),
    locations: axios.create({
        baseURL: config.LOCATIONS_API_URL,
    }),
    buses: axios.create({
        baseURL: config.BUSES_API_URL,
    }),
     
}