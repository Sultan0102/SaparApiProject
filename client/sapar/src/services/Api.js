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
    })
}