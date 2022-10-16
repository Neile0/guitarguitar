<template>
    <div>
        <p style="color:white;">Choose your Guitar</p>
        <ul style="color:white;">
            <button @click="change('youtube')" class="media_buttons"><img src="@/assets/youtube.png" width="50" height="50"></button>
            <button @click="change('spotify')" class="media_buttons"><img src="@/assets/spotify.png" width="50" height="50"></button>
        </ul>
        <div v-if="youtubeSelected">
            <YouTube :uri="currentMedia.youtube"/>
        </div>
        <div v-if="spotifySelected">7
            <Spotify :uri="currentMedia.spotify"/>
        </div>
        <div>
            <button style="margin-right:72px;" class="moveBtn" @click="next('left')">&#60;</button>
            <button class="likeBtn" @click="go()">Like</button>
            <button style="margin-left:72px;" class="moveBtn" @click="next('right')">&#62;</button>
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
                    this.i=0
                }
                
            } else {
                this.i -= 1
                if ( this.i < 0) {
                    this.currentMedia = this.media[this.media.length-1]
                    this.i = this.media.length
                } else {
                    this.currentMedia = this.media[this.i]
                }
                 
            }
            
        },
        go() {
            this.$router.push({name:'whatdoyoulike',params: {media:this.currentMedia}})
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
  .moveBtn {
    position: relative;
    width: 100px;
    height: 50px;
    font-weight:bold;
    background: #ffffff83;
    border-radius: 8px;
  }

  .moveBtn:hover{
    background: #ffffffda;
  }

  .likeBtn {
    position: relative;
    width: 150px;
    height: 50px;
    font-weight:bold;
    background: #ffffff83;
    border-radius: 8px;
  }

  .likeBtn:hover {
    background: #ffffffda;
  }

  h3 {
    margin: 40px 0 0;
  }
  p{
    font-size: 50px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    font-family: 'Courier New', Courier, monospace;
    color: black
  }
  ul {
    list-style-type: none;
    padding: 0;
    margin: none;
  }

  .media_buttons{
background-color: #33849cb6;
width: 220px;
  }

  .media_buttons:hover{
background-color: #33849c;

  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #8ba79b;
  }
  p{
    font-size: 50px;
    font-weight: 20px;
    font-family: 'Courier New', Courier, monospace;
    color: black
  }
  </style>
  