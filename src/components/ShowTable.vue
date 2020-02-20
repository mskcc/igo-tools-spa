<template>
    <md-table class="table">
        <md-table-row>
            <md-table-head>Name</md-table-head>
            <md-table-head>Server</md-table-head>
            <md-table-head class="doc-col">Documentation</md-table-head>
            <md-table-head >Description</md-table-head>
            <md-table-head></md-table-head>
        </md-table-row>
        <md-table-row v-for="tool in tools" :key="tool._id.$oid" :tool="tool">
            <md-table-cell>
                <a class="tool-name" :href="tool.link">{{ tool.name }}</a>
                <md-tooltip md-delay="300">{{ tool.tooltip }}</md-tooltip>
            </md-table-cell>
            <md-table-cell>
                <div class="tool-server">{{ tool.server }}</div>
            </md-table-cell>
            <md-table-cell class="doc-col">
                <!-- if tool.documentation.includes('github') {display with github icon} -->
                <div v-if="tool.documentation.includes(',')" class="tool-documentation">
                    <span v-for="(item, index) in tool.documentation.split(',')" :key="index">
                        <a :href="item">
                            <i v-if="item.includes('github')" class="fa-icon fab fa-github fa-3x"></i>
                            <i v-if="item.includes('plvpipetrack1')" class="fa-icon fas fa-book fa-3x"></i>
                            <md-tooltip md-delay="300">{{ item }}</md-tooltip>
                        </a>
                    </span>
                </div>
                <div v-else>
                    <a :href="item"><i class="fa-icon fas fa-link fa-2x"></i>
                        <md-tooltip md-delay="300">{{ item }}</md-tooltip>
                    </a>
                </div>
            </md-table-cell>
            
              <md-table-cell >
                <div class="tool-tooltip">{{ tool.tooltip }}</div>
            </md-table-cell>
            <md-table-cell class="edit-col">
                <md-button class="md-icon-button md-raised" v-on:click="handleEdit(tool)">
                    <md-icon>edit</md-icon>
                </md-button>
                <md-button class="md-icon-button md-raised" v-on:click="handleDelete(tool._id.$oid)">
                    <md-icon>delete</md-icon>
                    <!-- <i class='fab fa-github-square fa-3x'></i> -->
                </md-button>
            </md-table-cell>
        </md-table-row>
        <md-table-row>
            <md-table-cell colspan="6">A complete list of tools used internally by IGO.</md-table-cell>
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
            // if cancelling, set showDialog to false
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
th{
  width: 10px;
  font-size: 1.2em;
}
.table {
    text-align: left;
}
.doc-col {
    text-align: center;
}.edit-col {
    text-align: right;
}

i.fa-icon {
    margin-right: 5px;
}

.md-button.md-theme-default.md-raised:not([disabled]) {
    background-color: #e92076;
}

.md-icon.md-theme-default.md-icon-font {
    color: white;
}
</style>