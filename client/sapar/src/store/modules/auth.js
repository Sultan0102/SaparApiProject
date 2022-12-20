import axios from 'axios'
import AuthService from '@/services/AuthService';

const state = {
    user: null,
};

const getters = {
    isAuthenticated: state => !!state.user,
    StateUser: state => state.user,
};

const actions = {
    async Register({dispatch}, userForm) {
        let user = {
            email: userForm.get('email'),
            username: userForm.get('username'),
            password: userForm.get('password')
        }
        return AuthService.register(user).then(
            response => {
                let loginUserform = new FormData();
                loginUserform.append('email', userForm.getItem('email'));
                loginUserform.append('password', userForm.getItem('password'));

                dispatch('LogIn', loginUserform)

                return Promise.resolve(userForm.getItem('email'));
            },
            error => {
                return Promise.reject(error);
            }
        );
    },

    LogIn({commit}, userForm) {
        return AuthService.login(userForm.get('email'), userForm.get('password')).then(
            (responseData)=> {
            console.log(responseData.user)
            commit('setUser', responseData.user)
            return Promise.resolve()
        },
        error => {
            console.log(error)
            return Promise.reject(error)
        });
    },

    async LogOut({commit}){
        let user = null
        commit('LogOut', user)
    }
};

const mutations = {
    setUser(state, user){
        state.user = user
    },
    LogOut(state){
        state.user = null
        localStorage.removeItem('access-token')
    },
};

export default {
    state,
    getters,
    actions,
    mutations
}