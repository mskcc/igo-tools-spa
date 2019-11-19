<template>
  <div id='app'>
    <img alt='Vue logo' src='./assets/splash_logo_dark.png' />
    <p>A complete list of tools used internally by IGO</p>
    <!-- <HelloWorld msg='Welcome to Your Vue.js App' /> -->
    <new-tool></new-tool>
    <show-tools></show-tools>
    <!-- <button @click='$emit("addNewTool")'>Add new tool</button> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue';
import ShowTools from './components/ShowTools.vue';
import NewTool from './components/NewTool.vue';

export default {
  name: 'app',
  components: {
    // HelloWorld
    ShowTools,
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
