import Vuex from 'vuex';
import createPersistedState from "vuex-persistedstate";
import auth from './modules/auth'
import profile from './modules/profile'

const store = new Vuex.Store({
    modules: {
        auth,
        profile
    },
    plugins: [ createPersistedState() ]

});

export default store;