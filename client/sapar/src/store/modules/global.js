

const state = {
    current_language: 'en'
}

const getters = {
    getCurrentLanguage: state => state.current_language,
};

const actions = {
    
};

const mutations = {
    setCurrentLanguage(state, language) {
        state.current_language = language
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}   