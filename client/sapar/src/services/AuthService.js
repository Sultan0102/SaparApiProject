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
                TokenService.updateLocalAccessToken(response.data.access)
                TokenService.updateLocalRefreshToken(response.data.refresh)
            }
            return response.data
        });
    }

    logout() {
        TokenService.removeUser();
        TokenService.removeTokens();
    }

    register(user) {
        return Api.auth.post('register/', {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
            password: user.password,
            role: user.roleId
        });
    }

    registerBusinessPerson(user) {
        return Api.auth.post('register/', {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
            password: user.password,
            role: user.roleId,
            companyName: user.companyName,
            binNumber: user.binNumber,
            legalAddress: user.legalAddress,
        });
    }

    registerGuide(user) {
        return Api.auth.post('register/', {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
            password: user.password,
            role: user.roleId,
            specializations: user.specializations
        });
    }
    
    verify(email, code) {
        return Api.auth.post("verify/", {
            email,
            verificationCode: code
        });
    }
}


export default new AuthService()