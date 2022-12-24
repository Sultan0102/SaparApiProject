import AuthService from '@/services/AuthService';

const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: { loggedIn: false }, user: null };

const state = initialState

const getters = {
    isAuthenticated: state => !!state.user,
    StateUser: state => state.user,
};

const actions = {
    async register({ commit }, user) {
        return AuthService.register(user).then(
            response => {
                commit('registerSuccess')
                return Promise.resolve(userForm.getItem('email'));
            },
            error => {
                commit('registerFailure')
                return Promise.reject(error);
            }
        );
    },

    login({commit}, user) {
        return AuthService.login(user.email, user.password).then(
            (responseData)=> {
            commit('loginSuccess', responseData.user)
            return Promise.resolve()
        },
        error => {
            commit('loginFailure');
            return Promise.reject(error)
        });
    },

    logout({commit}){
        AuthService.logout();
        commit('logout')
    },

    refreshToken({ commit }, accessToken) {
        commit('refreshToken', accessToken)
    }
};

const mutations = {
    loginSuccess(state, user) {
        state.status.loggedIn = true;
        state.user = user;
    },
    loginFailure(state) {
        state.status.loggedIn = false;
        state.user = null;
    },
    logout(state) {
        state.status.loggedIn = false;
        state.user = null;
    },
    registerSuccess(state) {
        state.status.loggedIn = false;
    },
    registerFailure(state) {
        state.status.loggedIn = false;
    },
    refreshToken(state, accessToken) {
        state.status.loggedIn = true
        state.user = { ...state.user, accessToken: accessToken }  
    },
};

export default {
    state,
    getters,
    actions,
    mutations
}