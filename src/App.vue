<template>
    <div id="app">
        <div class="header">
            <img class="logo" alt="IGO logo" src="./assets/IGOlogo512.png" />
            <span>IGO Tools</span>
        </div>
        <nav>
            <ul>
                <li class="topnavli" v-for="link in links" :key="link">
                    <router-link exact :to="{ name: link }">{{ link }}</router-link>
                </li>
            </ul>
        </nav>
        <router-view></router-view>
    </div>
</template>
<script>
// import * as app from './app.js';

export default {
    name: "app",
    data: function() {
        return {
            links: ["home"]
        };
    },
    mounted() {
        this.$store.dispatch("setTools");
    }
};
</script>
<style>
@import "./assets/css/igo-tools.css";

.header {
    color: white;
    width: 100vw;
    text-align: left;
    padding: 1em;
    top: 0;
    background-color: #007cba;
}

.header img.logo {
    height: 3em;
    width: auto;
    margin-right: 1em;
}
</style>