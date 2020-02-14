import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import HomePage from "./components/pages/HomePage.vue";
// import CreateToolPage from "./components/pages/CreateToolPage.vue";
import store from "./store";

import VueSweetalert2 from "vue-sweetalert2";
// If you don't need the styles, do not connect
import "sweetalert2/dist/sweetalert2.min.css";
Vue.use(VueSweetalert2);

import "vue-material/dist/vue-material.min.css";
import "vue-material/dist/theme/default.css";
import {
    MdButton,
    MdContent,
    MdTabs,
    MdTable,
    MdIcon,
    MdTooltip
} from "vue-material/dist/components";

Vue.use(MdButton);
Vue.use(MdContent);
Vue.use(MdTabs);
Vue.use(MdTable);
Vue.use(MdIcon);
Vue.use(MdTooltip);
// Vue.use(MdApp);

Vue.use(VueRouter);

// it will ignore no-unused-vars
/* eslint-disable no-unused-vars */
const _ = require("lodash");
// then will re-enable

Vue.config.productionTip = false;

const routes = [
    { path: "/", component: HomePage, name: "home" },
    // { path: "/create", component: CreateToolPage, name: "create" }
];

const router = new VueRouter({
    routes: routes,
    mode: "history"
});

new Vue({
    store: store,
    router: router,
    render: h => h(App)
}).$mount("#app");
