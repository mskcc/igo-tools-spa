import Vue from "vue";
import Vuex from "vuex";

import * as app from "./../app.js";
import { _ } from "core-js";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        tools: [],
        toEdit: false,
        showDialog: false,
        editTool: { name: "", link: "", description: "" }
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
            app.axios.get("http://localhost:5000/getTools").then(response => {
                context.commit("setTools", response.data);
                // console.log(response);
                // console.log(response.data);
            });
        }
    }
});
