<template>
  <div>
    <div class='full-width'>
      <md-button class='md-primary md-raised igo-btn' @click='triggerDialog(true)'>Add Tool</md-button>
    </div>
    <md-dialog :md-active.sync='showDialog'>
      <md-dialog-title>New Tool</md-dialog-title>
      <md-dialog-actions>
        <form @submit.prevent='handleSubmit(tool)'>
          Name:
          <input type='text' v-model='tool.name' />
          <br />Link:
          <input type='text' v-model='tool.link' />
          <br />Tooltip:
          <input type='text' v-model='tool.tooltip' />
          <br />Location:
          <input type='text' v-model='tool.location' />
          <br />Documentation:
          <input type='text' v-model='tool.documentation' />
          <br />
          <md-button class='md-raised md-primary igo-btn' type='submit' value='Submit'>Submit</md-button>
          <!-- <button @submit.prevent='handleSubmit(tool)'>Submit</button> -->
          <!-- <input type='submit' value='Cancel' /> -->
          <md-button class='md-primary' @click='showDialog = false'>Close</md-button>
          <!--         <md-button class="md-primary" @click="showDialog = false">Save</md-button> -->
        </form>
      </md-dialog-actions>
    </md-dialog>
  </div>
</template>
<script>
import * as app from './../app.js';

export default {
  name: 'CreateToolPage',
  data: function() {
    return {};
  },
  computed: {
    tool: function() {
      return this.$store.state.editTool;
    },
    showDialog: {
      get: function() {
        return this.$store.state.showDialog;
      },
      set: function(bool) {
        return this.$store.commit('showDialog', bool);
      }
    },
    objectLength(state) {
      return Object.keys(this.$store.state.editTool).length;
    }
  },
  methods: {
    triggerDialog: function(bool) {
      if (this.$store.state.toEdit == false) {
        this.$store.commit('setEditTool', {
          name: '',
          link: '',
          tooltip: '',
          location: '',
          documentation: ''
        });
        return this.$store.commit('showDialog', bool);
      }
    },
    handleSubmit: function(tool) {
      // console.log(this.$store.state.editTool);
      // adds new tool
      console.log(this.$store.state.toEdit);
      if (this.$store.state.toEdit == false) {
        // this.$store.commit("setEditTool", {
        //   name: "",
        //   link: "",
        //   description: ""
        // });
        app.axios
          .post('http://localhost:5000/addTool', { ...tool })
          .then(response => {
            // set tools in Vuex store and route to home
            this.showDialog = false;
            this.$store.dispatch('setTools').then(() => {
              // this.$store.commit('setEditTool', '');
              // this.$router.push({
              //     name: 'home'
              // });
            });
          });
        // edits tool
      } else {
        app.axios
          .post('http://localhost:5000/editTool', { ...tool })
          .then(() => {
            this.$store.commit('setToEdit', false);
            // this.$store.commit('setEditTool', '');
            // this.$router.push({
            //     name: 'home'
            // });
          });
      }
    }
  }
};
</script>
<style scoped>
.full-width {
  width: 100%;
}
.md-button.md-primary.md-raised.md-theme-default.igo-btn {
  background-color: #007cba;
  margin-right: 0;
}
</style>
