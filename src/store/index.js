import Vue from "vue";
import Vuex from "vuex";

import * as app from "./../app.js";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        tools: [],
        toEdit: false,
        showDialog: false,
        editTool: { name: "", link: "", tooltip: "", server: "", documentation: "" }
    },
    mutations: {
        setTools(state, payload) {
            state.tools = payload;
        },
        setToEdit(state, payload) {
            state.toEdit = payload;
        },
        showDialog(state, payload) {
            state.showDialog = payload;
        },
        setEditTool(state, payload) {
            state.editTool = payload;
        }
    },
    actions: {
        setTools(context) {
            app.axios.get(process.env.VUE_APP_API_ROOT + "/getTools").then(response => {
                context.commit("setTools", response.data);
                // console.log(response);
                // console.log(response.data);
            });
        }
    }
});
