<template>
    <div class="hello">
        <iframe id="youtube_player" class="yt_player_iframe" width="420" height="315"
        :src="uri">
        </iframe>
    </div>
  </template>
  
  <script>
  export default {
    name: 'YouTube',
    props: {
      uri: String
    }
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
  