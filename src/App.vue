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
export default {
  name: 'app',
  data: function() {
    return {
      links: ['home', 'create']
    };
  }
};
</script>

<style>
@import './assets/css/igo-tools.css';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
