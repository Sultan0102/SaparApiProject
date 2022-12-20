import axios from 'axios'
import AuthService from '@/services/AuthService';
import UserService from '@/services/UserService';

const state = {
    userProfile: null
};

const getters = {
    getUserInfo: state => state.userProfile,
};

const actions = {
    UpdateProfileInfo({commit}, user) {
        console.log("Profile Info: ")
        console.log(user)
        return UserService.update(user).then(
            (userData)=> {
                commit('setUserProfile', userData)
                return Promise.resolve(userData)
            },
            (error)=> {
                return Promise.reject(error)
            }
        )
    },

    GetProfileInfo({commit}, id) {
        return UserService.retreive(id).then(
            (userData)=> {
                commit('setUserProfile', userData)
                return Promise.resolve(userData)
            },
            (error) => {
                return Promise.reject(error)
            }
        )
    }
};

const mutations = {
    setUserProfile({commit}, userData) {
        state.userProfile = userData
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}