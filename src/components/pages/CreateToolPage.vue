<template>
    <form @submit.prevent='handleSubmit(tool)'>
        Name:
        <input type='text' v-model='tool.name' />
        <br />Link:
        <input type='text' v-model='tool.link' />
        <br />Description:
        <input type='text' v-model='tool.description' />
        <br />
        <md-button class="md-raised md-primary" type='submit' value='Submit'>Submit</md-button>
        <!-- <button @submit.prevent='handleSubmit(tool)'>Submit</button> -->
        <!-- <input type='submit' value='Cancel' /> -->
    </form>
</template>
<script>
import * as app from './../../app.js';

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
            // console.log(this.$store.state.editTool);
            // adds new tool
            if (this.$store.state.toEdit == false) {
                app.axios
                    .post('http://localhost:5000/addTool', { ...tool })
                    .then(response => {
                        // set tools in Vuex store and route to home
                        this.$store.dispatch('setTools').then(() => {
                            // this.$store.commit('setEditTool', '');
                            this.$router.push({
                                name: 'home'
                            });
                        });
                    });
                // edits tool
            } else {
                app.axios
                    .post('http://localhost:5000/editTool', { ...tool })
                    .then(() => {
                        this.$store.commit('setToEdit', false);
                        // this.$store.commit('setEditTool', '');
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