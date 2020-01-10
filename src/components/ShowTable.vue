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
      <tr v-for='tool in tools' :key='tool.id' :tool='tool'>
        <td>
          <div class='tool-name'>{{ tool.name }}</div>
        </td>
        <td>
          <a class='tool-link' :href='tool.link'>{{ tool.link }}</a>
        </td>
        <td>
          <div class='tool-description'>{{ tool.description }}</div>
        </td>
        <td>
          <button>Edit</button>
        </td>
        <td>
          <button>Delete</button>
        </td>
      </tr>
    </table>
  </div>
</template> 


<script>
// import { tools } from './../tools.js';
const axios = require('axios');

export default {
  name: 'ShowTable',
  data: function() {
    return {
      tools: []
    };
  },
  mounted() {
    axios.get('http://localhost:5000/getTools').then(response => {
      this.tools = response.data;
      console.log(response);
      console.log(response.data);
    });
  }
};
</script>

<style scoped>
</style>