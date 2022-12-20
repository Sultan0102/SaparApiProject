import axios from 'axios'
import config from '../../configuration/dev.env'
import store from '@/store/index'


export default {
    authBase: axios.create({
        baseURL: config.AUTH_API_URL
    }),
    auth: axios.create({
        baseURL: config.AUTH_API_URL,
        headers: {
            'Authorization': `Bearer ${localStorage.getItem("access-token")}`
        }
    }),
    users: axios.create({
        baseURL: config.USERS_API_URL,
        headers: {
            'Authorization': `Bearer ${localStorage.getItem("access-token")}`
        }
    }),
    tickets: axios.create({

    })
}