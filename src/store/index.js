import Vue from 'vue'
import Vuex from 'vuex'

import * as app from './../app.js'
import { _ } from 'core-js'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        tools: [],
    },
    mutations: {
        setTools(state, payload) {
            state.tools = payload
        },
        // install lodash before using this
        // addTool(state, payload) {
        //     _.merge(state.tools, payload.tool)
        //     // console.log(payload)
        //     console.log(state.tools)
        // }
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