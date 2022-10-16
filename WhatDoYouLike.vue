<template> 
    <div>
        <h1>What Do You Like</h1>
        <div class="buttons_what_do_you_like">
          <div id="rectangle1">
          <!--<a target="_blank" href="guitar.png">-->
            <img :src="require('@/assets/guitar.png')" alt="guitar" width="200" height="400">
          <!--</a>-->
        </div>
        <div id="rectangle2">
          <img :src="require('@/assets/guitar.png')" alt="guitar" width="200" height="400">
        </div>
        <div id="rectangle3"></div>
        <!---
        <div v-show="youtubeSelected">
            <YouTube/>
        </div>
        <div v-show="spotifySelected">7
            <Spotify :uri="myVar"/>
        </div>
        <div>
        <button @click="changemyVar()">Like</button>
        </div>
        -->
        </div>
        
    </div>
</template>
  <!--
  <script>
  import YouTube from './YouTube.vue'
import Spotify from './Spotify.vue'
  export default {
    name: 'WhatDoYouLike',
    components: {
        YouTube,
        Spotify
    },
    props: {
      msg: String
    },
    data () {
        return {
            youtubeSelected: true,
            spotifySelected:false,
            myVar:"https://open.spotify.com/embed/track/4vsoWZcvtvSsE0OiVvDDvX?si=e0c9477964664276"
        }
    },
    methods: {
        go() {
            this.$router.push()
        },
        changemyVar() {
            this.myVar ="https://open.spotify.com/embed/track/1Ud6moTC0KyXMq1Oxfien0?si=c565fd4210664132"
        },
        change(string) {
            if ( string == "youtube" ) {
                this.youtubeSelected = true
                this.spotifySelected = false
            } else {
                this.youtubeSelected = false
                this.spotifySelected = true 
            }
        }
    }
  }
  </script>
  -->
  
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

  #rectangle1{
  border-radius: 25px;
  background: #767676;
  opacity: 0.5;
  padding: 20px;
  width: 200px;
  height: 400px;
  position: absolute;
  top: 150px;
  left: 200px
  }
  #rectangle2{
  border-radius: 25px;
  background: #767676;
  opacity: 0.5;
  padding: 20px;
  width: 200px;
  height: 400px;
  position: absolute;
  top: 150px;
  left: 500px
  }
  #rectangle3{
  border-radius: 25px;
  background: #767676;
  opacity: 0.5;
  padding: 20px;
  width: 200px;
  height: 400px;
  position: absolute;
  top: 150px;
  left: 800px
  }
  </style>
  