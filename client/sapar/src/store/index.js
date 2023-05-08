import Vuex from 'vuex';
import auth from './modules/auth'
import global from './modules/global'

const store = new Vuex.Store({
    modules: {
        auth,
        global
    },
    plugins: []

});

export default store;