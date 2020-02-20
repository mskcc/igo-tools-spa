<template>
<div>
    <div class='full-width'>
        <md-button class='md-fab igo-btn' @click='triggerDialog(true)'>
            <md-icon>add</md-icon>
        </md-button>
    </div>
    <md-dialog :md-active.sync='showDialog' @md-closed='resetToEdit(false)'>
        <md-dialog-title>New Tool</md-dialog-title>
        <md-dialog-actions>
            <form @submit.prevent='handleSubmit(tool)'>
                <md-field>
                    <label>Name</label>
                    <md-input required type='text' v-model='tool.name'></md-input>
                </md-field>
                <md-field>
                    <label>Link</label>
                    <md-input required type='text' v-model='tool.link'></md-input>
                </md-field>
                <md-field>
                    <label>Description</label>
                    <md-input type='text' v-model='tool.tooltip'></md-input>
                </md-field>
                <md-field>
                    <label>Documentation link</label>
                    <md-input type='text' v-model='tool.documentation'></md-input>
                </md-field>
                <!-- <input required type='text' v-model='tool.name' /> -->
                <!-- <br />Link:
          <input type='text' v-model='tool.link' />
          <br />Tooltip:
          <input type='text' v-model='tool.tooltip' />-->
                <label>Server</label>
                <br />
                <md-checkbox v-model='tool.server' :value='obj1'>pitchfork</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj2'>alba</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj3'>bic</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj4'>igo vm</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj5'>igodev vm</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj6'>tango</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj7'>igolims</md-checkbox>
                <md-checkbox v-model='tool.server' :value='obj8'>delphi</md-checkbox>
                <!-- <br />Documentation:
          <input type='text' v-model='tool.documentation' />
          <br />-->
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
        return {
            obj1: 'pitchfork',
            obj2: 'alba',
            obj3: 'bic',
            obj4: 'igovm',
            obj5: 'igodev',
            obj6: 'tango',
            obj7: 'igolims',
            obj8: 'delphi'
        };
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

    },
    methods: {
        resetToEdit: function(bool) {
            this.$store.commit('setToEdit', bool);
            this.$store.dispatch('setTools');
        },
        triggerDialog: function(bool) {
            // console.log(this.$store.state.toEdit);
            if (this.$store.state.toEdit == false) {
                this.$store.commit('setEditTool', {
                    name: '',
                    link: '',
                    tooltip: '',
                    server: '',
                    documentation: ''
                });
                // console.log(this.$store.state.toEdit);
                return this.$store.commit('showDialog', bool);
            }
        },
        handleSubmit: function(tool) {
            // console.log(this.$store.state.editTool);
            // adds new tool
            // console.log(this.$store.state.toEdit);
            if (this.$store.state.toEdit == false) {
                // this.$store.commit("setEditTool", {
                //   name: "",
                //   link: "",
                //   description: ""
                // });
                app.axios
                    .post('http://localhost:5000/addTool', { ...tool })
                    .then(() => {
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
                        this.$store.commit('showDialog', false);
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

.md-button.md-theme-default.md-fab:not([disabled]) {
    background-color: #007cba;
}
</style>