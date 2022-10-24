import Vuex from 'vuex';
import createPersistedState from "vuex-persistedstate";
import auth from './modules/auth'

const store = new Vuex.Store({
    modules: {
        auth,
    },
    plugins: [ createPersistedState() ]

});

export default store;