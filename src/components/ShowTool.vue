<template>
  <div class='tool'>
    <table>
      <tr>
        <td>
          <div class='tool-name'>{{ tool.name }}</div>
        </td>
        <td>
          <a class='tool-link' :href='tool.link'>{{ tool.link }}</a>
        </td>
        <td>
          <div class='tool-description'>Description{{ tool.description }}</div>
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

export default {
  name: 'ShowTool',
  props: ['tool']
};
</script>

<style scoped>
</style>