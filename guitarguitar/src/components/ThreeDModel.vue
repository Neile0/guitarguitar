<template>
    <div class="hello">
        <model-viewer v-if="isMounted" disable-tap auto-rotate shadow-intensity="1" camera-controls interaction-prompt="none" rotation-per-second = "15deg" touch-action="pan-y" :src="uri" :poster="poster" ar ar-modes="webxr scene-viewer quick-look"></model-viewer>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ThreeDModel',
    props: {
      uri: String,
      poster: String,
    },
    data (){
      return{
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
  