<template>
  <md-table class="table">
    <md-table-row>
      <md-table-head>Name</md-table-head>
      <md-table-head>Link</md-table-head>
      <md-table-head>Location</md-table-head>
      <md-table-head>Documentation</md-table-head>
      <md-table-head>Edit</md-table-head>
      <md-table-head>Delete</md-table-head>
    </md-table-row>
    <md-table-row v-for="tool in tools" :key="tool._id.$oid" :tool="tool">
      <md-table-cell>
        <div class="tool-name">{{ tool.name }}</div>
      </md-table-cell>
      <md-table-cell>
        <a class="tool-link" :href="tool.link">{{ tool.link }}</a>
      </md-table-cell>
      <md-table-cell>
        <div class="tool-location">{{ tool.location }}</div>
      </md-table-cell>
      <md-table-cell>
        <!-- if tool.documentation.includes('github') {display with github icon}-->
        <div class="tool-documentation">{{ tool.documentation }}</div>
      </md-table-cell>
      <md-table-cell>
        <button v-on:click="handleEdit(tool)">
          <md-icon>edit</md-icon>
        </button>
      </md-table-cell>
      <md-table-cell>
        <button v-on:click="handleDelete(tool._id.$oid)">
          <md-icon>delete</md-icon>
        </button>
      </md-table-cell>
      <md-tooltip md-delay="300">{{ tool.tooltip }}</md-tooltip>
    </md-table-row>
    <md-table-row>
      <md-table-cell colspan="6"
        >A complete list of tools used internally by IGO.</md-table-cell
      >
    </md-table-row>
  </md-table>
</template>
<script>
import * as app from "./../app.js";

export default {
  name: "ShowTable",
  data: function() {
    return {};
  },
  methods: {
    handleDelete: function(id) {
      let toolToDelete = this.$store.state.tools.find(
        tool => (tool._id.$oid = id)
      );

      this.$swal
        .fire({
          text: "Are you sure you want to delete " + toolToDelete.name + "?",
          // html: response.data,
          // footer: 'To avoid mistakes, invalid cells are cleared immediately.',
          type: "info",
          animation: false,
          showCancelButton: true,
          confirmButtonText: "Okay!",
          confirmButtonColor: "#df4602",
          cancelButtonColor: "#007cba"
          // customClass: { content: 'alert' },
        })
        .then(result => {
          if (result.value) {
            // delete by id
            app.axios
              .post("http://localhost:5000/deleteTool", { id })
              .then(response => {
                if (response) {
                  // sets tools in Vuex store and routes to home
                  this.$store.dispatch("setTools");
                }
              })
              .catch(error => {
                return error;
              });
            return;
            // } else if (result.dismiss) {
          } else {
            return;
          }
        });
    },
    handleEdit: function(tool) {
      // console.log(tool);
      // console.log(this.$store.state.tools);

      // stores editTool and routes to create page to display form

      this.$store.commit("setEditTool", tool);
      this.$store.commit("setToEdit", true);
      this.$store.commit("showDialog", true);
      // this.$router.push({ name: "create" });
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
.table {
  text-align: left;
}
</style>
