import Api from "./Api"
import store from '@/store/index'
import axios from "axios";


class AuthService {
    login(email, password) {
        return Api.authBase.post('login/', {
            email: email,
            password: password
        }).then(function (response) {
            console.log(response)
            if(response.data.access) {
                localStorage.setItem('access-token', response.data.access);
            }
            return response.data
        });
    }

    logout() {
        localStorage.removeItem('user')
    }

    register(user) {
        // TODO: Get rid of required 'username' field
        return Api.authBase.post('register/', {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
            password: user.password,
            
            username: user.email,
        });
    }
}


export default new AuthService()