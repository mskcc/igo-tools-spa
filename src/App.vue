<template>
  <div id='app'>
    <h1>IGO Tools</h1>
    <img alt='IGO logo' src='./assets/splash_logo_dark.png' />
    <p>A complete list of tools used internally by IGO</p>

    <new-tool></new-tool>
    <home-page></home-page>
    <!-- <button @click='$emit("addNewTool")'>Add new tool</button> -->
  </div>
</template>

<script>
import HomePage from './components/pages/HomePage.vue';
import NewTool from './components/NewTool.vue';

export default {
  name: 'app',
  components: {
    HomePage,
    NewTool
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
