<template>
  <div id='tools' class='grid-container grid-container--fit'>
    <show-table></show-table>
  </div>
</template>

<script>
import ShowTable from './../ShowTable.vue';

export default {
  name: 'HomePage',
  components: { ShowTable }
};
</script>

<style scoped>
table {
  border: 1px solid black;
}
</style>