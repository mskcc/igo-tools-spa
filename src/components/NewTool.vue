<template>
    <div>
        <button @click='addNewTool'>Add new tool</button>
        <form v-if='newTool'>
            
            <label>Name of new tool:</label>
            <input type='text' v-model.lazy='newToolName'></input>
            </br>
            <label>Link:</label>
            <input type='text' v-model.lazy='newToolLink'></input>
            </br>
            <label>Description:</label>
            <input type='text' v-model.lazy='newToolDescription'>
            </br>
            <button @click='done'>done</button>
          
        </form>
    </div>
</template>


<script>
export default {
  name: 'NewTool',
  data: function() {
      return {
          newTool: false,
          newToolName: "",
          newToolLink: "",
          newToolDescription: ""
      }
  },
  methods: {
    addNewTool: function() {
        this.newTool = !this.newTool;
    },
    done: function() {
        console.log(this.newToolName)
    }
  },
};
</script>

<style scoped>
</style>