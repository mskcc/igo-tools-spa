<template>
  <div class='tool'>
    <table style='width:100%'>
      <tr>
        <th>Name</th>
        <th>Link</th>
        <th>Description</th>
        <th>Edit</th>
        <th>Delete</th>
      </tr>
      <tr v-for='tool in tools' :key='tool._id.$oid' :tool='tool'>
        <td>
          <div class='tool-name'>{{ tool.name}}</div>
        </td>
        <td>
          <a class='tool-link' :href='tool.link'>{{ tool.link }}</a>
        </td>
        <td>
          <div class='tool-description'>{{ tool.description }}</div>
        </td>
        <td>
          <button v-on:click='handleEdit(tool._id.$oid)'>Edit</button>
        </td>
        <td>
          <button v-on:click='handleDelete(tool.name)'>Delete</button>
        </td>
      </tr>
    </table>
  </div>
</template> 


<script>
import * as app from './../app.js';
// const axios = require('axios');

export default {
  name: 'ShowTable',
  data: function() {
    return {};
  },
  methods: {
    handleDelete: function(name) {
      console.log(name);
      // delete by id
      app.axios
        .post('http://localhost:5000/deleteTool', { name })
        .then(response => {
          // Set tools in Vuex store and route to home
          this.$store.dispatch('setTools').then(() =>
            this.$router.push({
              name: 'home'
            })
          );
        });
    },
    handleEdit: function() {}
  },
  computed: {
    tools: function() {
      return this.$store.state.tools;
    }
  }
};
</script>

<style scoped>
</style>