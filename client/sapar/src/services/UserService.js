import Api from "./Api"
import store from '@/store/index'
import axios from "axios";
import TokenService from "./TokenService";


class UserService {
    retreive(id) {
        return Api.users.get(`${id}/`).then(function(response) {
            return response.data;
        })
    }

    update(user) {
        return Api.users.put(`${user.id}/`, {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
        })
    }

    updateLocalUser(user) {
        let currentUser = TokenService.getUser();
        currentUser.email = user.email;
        currentUser.firstName = user.firstName;
        currentUser.lastName = user.lastName;

        TokenService.setUser(currentUser);
        // store.dispatch("")

    }
}


export default new UserService()