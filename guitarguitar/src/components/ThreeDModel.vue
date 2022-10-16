<template>
    <div class="hello">
<<<<<<< HEAD
        <model-viewer v-if="isMounted" disable-tap auto-rotate shadow-intensity="1" camera-controls interaction-prompt="none" rotation-per-second = "15deg" touch-action="pan-y" src="/guitarThreeD.glb" ar ar-modes="webxr scene-viewer quick-look"></model-viewer>
=======
        <model-viewer v-if="isMounted" :src="uri" camera-controls></model-viewer>
>>>>>>> f09701eb15a53f41ee762005618f6ef0b4923aab
    </div>
  </template>
  
  <script>
  export default {
    name: 'ThreeDModel',
    props: {
      uri: String
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
  