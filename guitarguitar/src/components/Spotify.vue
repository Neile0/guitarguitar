<template>
    <div class="hello">
        <iframe class = "soptifyIframe" style="border-radius:12px" width=600 height=500 :src="uri" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SpotifyT',
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
  