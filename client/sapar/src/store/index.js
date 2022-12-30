import Vuex from 'vuex';
import auth from './modules/auth'
import profile from './modules/profile'

const store = new Vuex.Store({
    modules: {
        auth,
        profile
    },
    plugins: []

});

export default store;