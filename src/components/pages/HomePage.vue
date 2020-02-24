<template>
    <div id="tools" class="grid-container grid-container--fit">
        <create-tool></create-tool>
        <show-table></show-table>
    </div>
</template>

<script>
import ShowTable from "./../ShowTable.vue";
import CreateTool from "./../CreateTool.vue";

export default {
    name: "HomePage",
    components: { ShowTable, CreateTool }
};
</script>

<style scoped>
table {
    border: 1px solid black;
}
#tools {
    width: 90vw;
    margin: 0 auto;
    text-align: right;
}
</style>
