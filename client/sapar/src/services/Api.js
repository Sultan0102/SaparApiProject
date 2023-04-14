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
     
}