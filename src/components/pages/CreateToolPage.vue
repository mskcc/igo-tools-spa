<template>
  <form @submit.prevent='handleSubmit(tool)'>
    Name:
    <input type='text' v-model='tool.name' />
    <br />Link:
    <input type='text' v-model='tool.link' />
    <br />Description:
    <input type='text' v-model='tool.description' />
    <br />
    <input type='submit' value='Submit' />
    <input type='submit' value='Cancel' />
  </form>
</template>

<script>
import * as app from './../../app.js';

// let tool = {};
// If in dev mode, we pre-fill the tool to make demo/testing easier
// if (process.env.NODE_ENV == 'development') {
//   tool = {
//     // id: 3,
//     name: 'test',
//     link: 'test.com',
//     description: 'test'
//   };
// } else if (this.$store.editTool) {
//   tool = this.$store.editTool;
// } else {
//   tool = {
//     // id: '',
//     name: '',
//     link: '',
//     description: ''
//   };
// }

export default {
  name: 'CreateToolPage',
  data: function() {
    return {};
  },
  computed: {
    tool: function() {
      return this.$store.state.editTool;
    },
    objectLength(state) {
      return Object.keys(this.$store.state.editTool).length;
    }
  },
  methods: {
    handleSubmit: function(tool) {
      // console.log(tool);
      // if (objectLength(this.$store.state.editTool)) {
      //   app.axios
      //     .post('http://localhost:5000/editTool', { ...tool })
      //     .then(() => {
      //       this.$store.commit('setEditTool', null);
      //       this.$router.push({
      //         name: 'home'
      //       });
      //     });
      // } else {
      //   app.axios
      //     .post('http://localhost:5000/addTool', { ...tool })
      //     .then(response => {
      //       // Set tools in Vuex store and route to home
      //       this.$store.dispatch('setTools').then(() => {
      //         // this.$store.commit('setEditTool', null);
      //         this.$router.push({
      //           name: 'home'
      //         });
      //       });
      //     });
      // }
      console.log(this.$store.state.editTool);
      if (this.$store.state.toEdit == false) {
        app.axios
          .post('http://localhost:5000/addTool', { ...tool })
          .then(response => {
            // Set tools in Vuex store and route to home
            this.$store.dispatch('setTools').then(() => {
              // this.$store.commit('setEditTool', null);
              this.$router.push({
                name: 'home'
              });
            });
          });
      } else {
        app.axios
          .post('http://localhost:5000/editTool', { ...tool })
          .then(() => {
            this.$store.commit('setToEdit', false);
            this.$router.push({
              name: 'home'
            });
          });
      }
    }
  }
};
</script>

<style scoped>
</style>