
let currentLang = localStorage.getItem('currentLanguage')

const state = {
    current_language: currentLang ?? 'en'
}

const getters = {
    getCurrentLanguage: state => state.current_language,
};

const actions = {
    
};

const mutations = {
    setCurrentLanguage(state, language) {
        state.current_language = language
        localStorage.setItem('currentLanguage', language)
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}   