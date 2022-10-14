<template>
  <div id="app">
    <VideoScreen/>
  </div>
</template>

<script>
import VideoScreen from './components/VideoScreen.vue'
export default {
  name: 'App',
  components: {
    VideoScreen
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
