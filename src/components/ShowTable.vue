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
          <button v-on:click='handleEdit(tool)'>Edit</button>
        </td>
        <td>
          <button v-on:click='handleDelete(tool._id.$oid)'>Delete</button>
        </td>
      </tr>
    </table>
  </div>
</template> 


<script>
import * as app from './../app.js';

export default {
  name: 'ShowTable',
  data: function() {
    return {};
  },
  methods: {
    handleDelete: function(id) {
      console.log(id);
      // delete by id
      app.axios
        .post('http://localhost:5000/deleteTool', { id })
        .then(response => {
          // sets tools in Vuex store and routes to home
          this.$store.dispatch('setTools');
        });
    },
    handleEdit: function(tool) {
      // console.log(tool);
      // console.log(this.$store.state.tools);

      // stores editTool and routes to create page to display form
      this.$store.commit('setEditTool', tool);
      this.$store.commit('setToEdit', true);
      this.$router.push({ name: 'create' });
    }
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