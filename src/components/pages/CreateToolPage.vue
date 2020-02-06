<template>
  <form @submit.prevent='handleSubmit'>
    Name:
    <input type='text' v-model='tool.name' />
    <br />Link:
    <input type='text' v-model='tool.link' />
    <br />Description:
    <input type='text' v-model='tool.description' />
    <br />
    <input type='submit' value='Submit' />
  </form>
</template>

<script>
import * as app from './../../app.js';

let tool = {};
// If in dev mode, we pre-fill the tool to make demo/testing easier
if (process.env.NODE_ENV == 'development') {
  tool = {
    // id: 3,
    name: 'test',
    link: 'test.com',
    description: 'test'
  };
} else {
  tool = {
    // id: '',
    name: '',
    link: '',
    description: ''
  };
}

export default {
  name: 'CreateToolPage',
  data: function() {
    return {
      tool: tool
    };
  },
  methods: {
    handleSubmit: function() {
      app.axios
        .post('http://localhost:5000/addTool', this.tool)
        // .post('./../../igo-tools-backend/app/toollist.py')
        .then(response => {
          // let id = Date.now();
          // console.log(id);
          // Update Vuex store
          this.$store.dispatch('setTools').then(() =>
            this.$router.push({
              name: 'home'
            })
          );

          // push to the homepage with newly added tool
        });
    }
  }
};
</script>

<style scoped>
</style>