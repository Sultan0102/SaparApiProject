import Api from "./Api"
import store from '@/store/index'
import axios from "axios";
import TokenService from "./TokenService";
import router from "../../router/router"

class AuthService {

    login(email, password) {
        return Api.auth.post('login/', {
            email: email,
            password: password
        }).then(function (response) {
            if(response.data.user) {
                TokenService.setUser(response.data.user)
            }
            return response.data
        });
    }

    logout() {
        router.push('/home')
        TokenService.removeUser();
    }

    register(user) {
        // TODO: Get rid of required 'username' field
        return Api.auth.post('register/', {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
            password: user.password,
            
            username: user.email,
        });
    }
}


export default new AuthService()