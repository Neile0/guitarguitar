<template>
    <div>
        <h1>Choose your Guitar</h1>
        <ul style="">
            <li @click="change('youtube')">Youtube</li>
            <li @click="change('spotify')">Spotify</li>
        </ul>
        <div v-show="youtubeSelected">
            <YouTube :uri="currentMedia.youtube"/>
        </div>
        <div v-show="spotifySelected">7
            <Spotify :uri="currentMedia.spotify"/>
        </div>
        <div>
            <button @click="next('left')">&#60;</button>
            <button @click="go()">Like</button>
            <button @click="next('right')">&#62;</button>
        </div>
    </div>
</template>
  
  <script>
  import YouTube from './YouTube.vue'
  import Spotify from './Spotify.vue'
  import axios from 'axios'
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
            currentMedia: {},
            i:0
        }
    },
    mounted () {
        axios.get("http://localhost:8000/api/media")
        .then((response) => {
            this.media = response.data
            this.currentMedia = this.media[0]
            this.i = 0
            console.log(this.currentMedia)
        })
    },
    methods: {
        next(str) {
            if (str == 'right') {
                this.i += 1
                if ( this.i < this.media.length) {
                    this.currentMedia = this.media[this.i]
                } else {
                    this.currentMedia = this.media[0]
                }
                
            } else {
                this.i -= 1
                if ( this.i < 0) {
                    this.currentMedia = this.media[this.media.length-1]
                } else {
                    this.currentMedia = this.media[this.i]
                }
                 
            }
            
        },
        go() {
            this.$router.push({name:'whatdoyoulike',params: {media:this.media}})
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
  