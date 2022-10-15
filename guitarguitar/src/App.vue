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
  background: linear-gradient(60deg, #565656, #84eef8);
}
html, body {
    height: 100%;
    margin: 0;
    padding: 0;
  }
body {
  background-color: rgb(70, 70, 70);
}
</style>
