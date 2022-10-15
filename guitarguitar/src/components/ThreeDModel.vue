<template>
    <div class="hello">
      <model-viewer v-if="isMounted" src="/models/guitar150929289678002.glb" camera-controls></model-viewer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ThreeDModel',
    props: {
      uri: String
    },
    data () {
      return {
        src: "@/assets/guitar150929289678002.glb",
        isMounted: false
      }
    },
    mounted () {
      this.isMounted = true
      this.loadComponent()
    },
    computed: {
    loadComponent() {
      return () => import('@google/model-viewer');
    }
  },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  