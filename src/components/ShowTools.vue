<template>
  <div id='tools' class='grid-container grid-container--fit' >
    <!-- <h2>Tools</h2> -->
    <show-tool v-for='tool in tools' :key='tool.id' :tool='tool'></show-tool>
  </div>
</template>

<script>
import ShowTool from './ShowTool.vue';
// import { tools } from './../tools.js';

export default {
  name: 'ShowTools',
  components: { ShowTool },
  data: function() {
    return {
      tools: [
        {
          id: 1,
          name: 'BAM QC review- Website',
          link: 'https://igo.mskcc.org/seq-qc/home',
          description: ''
        },
        {
          id: 2,
          name: 'Confluence - Work Requests for Data Team',
          link:
            'http://plvpipetrack1.mskcc.org:8099/pages/viewpage.action?spaceKey=IDT&title=Work+Requests+for+Data+Team',
          description: ''
        },
        {
          id: 3,
          name: 'Email Template',
          link:
            'https://docs.google.com/document/d/1mpE5fhbwSEAeyj4kZe6UZ_QjafbETHfQisB17dxWo0E/edit',
          description: ''
        },
        {
          id: 4,
          name: 'FastQ Delivery Stats',
          link: 'http://seq.cbio.mskcc.org:3000/testing/fastqRunStats/',
          description: ''
        },
        {
          id: 5,
          name: 'FastQC',
          link: 'http://seq.cbio.mskcc.org/lims/fastqc',
          description: ''
        },
        {
          id: 6,
          name: 'Hiseq Log',
          link: 'http://alba.cbio.mskcc.org:3004/hiseq_logs',
          description: ''
        },
        {
          id: 7,
          name: 'Hiseq Project Log',
          link:
            'https://docs.google.com/spreadsheets/d/1kHQU-AzDBz5ve4y2ZpZh0FC176wnjk5ZudssLCuZBtg/edit?invite=CIP4gJMC&pli=1#gid=839974327',
          description: ''
        }
      ]
    }
  }
};
</script>

<style scoped>
</style>