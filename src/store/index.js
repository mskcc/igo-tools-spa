import Vue from 'vue'
import Vuex from 'vuex'

import * as app from './../app.js'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        tools: [],
    },
    mutations: {
        setTools(state, payload) {
            state.tools = payload
        }
    },
    actions: {
        setTools(context) {
            app.axios.get('http://localhost:5000/getTools').then(response => {
                context.commit('setTools', response.data);
                // console.log(response);
                // console.log(response.data);
            })
        }
    }
})