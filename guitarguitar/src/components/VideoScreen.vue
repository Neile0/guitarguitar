<template>
    <div>
        <h1>Choose your Guitar</h1>
        <ul style="">
            <li @click="change('youtube')">Youtube</li>
            <li @click="change('spotify')">Spotify</li>
        </ul>
        <div v-show="youtubeSelected">
            <YouTube/>
        </div>
        <div v-show="spotifySelected">7
            <Spotify :uri="myVar"/>
        </div>
        <div>
        <button @click="changemyVar()">Like</button>
        </div>
    </div>
</template>
  
  <script>
  import YouTube from './YouTube.vue'
import Spotify from './Spotify.vue'
  export default {
    name: 'VideoScreen',
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
  