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

    retreiveGuides() {
        return Api.guides.get().then(
            (response) => {
                return response.data;
            }
        )
    }

    retreiveGuide(id) {
        return Api.guides.get(`${id}/`).then(
            (response) => {
                return response.data
            }
        )
    }

    retreiveDriverByUserId(id) {
        return Api.drivers.get(`${id}/`).then(
            (response) => {
                return response.data
            }
        )
    }

    retreiveDriverById(id) {
        return Api.drivers.get(`${id}/`).then(
            (response) => {
                return response.data
            }
        )
    }

    retreiveGuideByUserId(userId) {
        return Api.guides.post(`user/`, {
            userId
        }).then(
            (response)=> {
                return response.data
            }
        )
    }

    update(user) {
        return Api.users.put(`${user.id}/`, {
            email: user.email,
            firstName: user.firstName,
            lastName: user.lastName,
        })
    }

    updateDriver(driver) {
        return Api.drivers.put(`${driver.id}/`, driver).then(
            (response)=> {
                return response.data
            }
        )
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