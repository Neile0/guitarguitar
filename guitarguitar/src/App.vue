<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
//import ResultsScreen from './components/ResultsScreen.vue'
export default {
  name: 'App',
  components: {
  
  }
}
</script>

<style>
#app {

  height:100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
html, body {
    height: 100%;
    margin: 0;
    padding: 0;
    background: linear-gradient(to right, #2C5364, #203A43, #0F2027);
  }
  /**
body {
  background: linear-gradient(60deg, #e3ff0f, #fb8918);
}
*/
</style>
