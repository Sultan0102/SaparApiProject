import Api from "./Api"
import store from '@/store/index'
import axios from "axios";


class UserService {
    retreive(id) {
        return Api.users.get(`${id}/`).then(function(response) {
            return response.data;
        })
    }

    update(user) {
        return Api.users.put(`${user.id}/`, {
            firstName: user.firstName,
            lastName: user.lastName,
            email: user.email,
        })
    }
}


export default new UserService()