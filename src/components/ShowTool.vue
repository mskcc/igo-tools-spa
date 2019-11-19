<template>
  <div class='tool'>
    <div class='tool-name'>{{ tool.name }}</div>
    <a class='tool-link' :href='tool.link'>{{ tool.link }}</a>
    <div class='tool-description'>Description{{ tool.description }}</div>
    <button>Edit</button>
    <button>Delete</button>
  </div>
</template> 


<script>
// import { tools } from './../tools.js';

export default {
  name: 'ShowTool',
  props: ['tool']
};
</script>

<style scoped>
</style>