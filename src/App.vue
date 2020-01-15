<template>
  <div id='app'>
    <h1>IGO Tools</h1>
    <img alt='IGO logo' src='./assets/splash_logo_dark.png' />
    <p>A complete list of tools used internally by IGO</p>
    <nav>
      <ul>
        <li class='topnavli' v-for='link in links' :key='link'>
          <router-link exact :to='{ name: link }'>{{ link }}</router-link>
        </li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
// import * as app from './app.js';

export default {
  name: 'app',
  data: function() {
    return {
      links: ['home', 'create']
    };
  },
  mounted() {
    this.$store.dispatch('setTools');
  }
};
</script>

<style>
@import './assets/css/igo-tools.css';
</style>
