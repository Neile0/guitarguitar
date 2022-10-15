<template>
    <div>
        <div>
            <div id="guitarImg" style="float:left;text-align:left;border:1px solid grey;width:400px;height:600px;">
                <img width=400 height=600 src="https://upload.wikimedia.org/wikipedia/commons/6/63/Fender_Stratocaster_004-2.jpg"/>
            </div>
            <div id="guitarInfo">
                <p>Make:{{make}}</p>
                <p>Model: {{model}}</p>
                <p>Guitarists: {{guitarists}} </p>
            </div>
            <div id="social">
                
                <Spotify :uri="currentMedia.spotify"/>
                <YouTube :uri="currentMedia.youtube"/>
            </div>
        </div>
    </div>
</template>
  
  <script>
  import Spotify from './Spotify.vue'
  import YouTube from './YouTube.vue'
  import axios from 'axios'
  export default {
    name: 'ResultsScreen',
    components: {
      Spotify,
      YouTube
    },
    props: ['type','media'],
    data () {
        return {
            make: "Fender",
            model: "Stratocaster",
            guitarists: "Eric Clapton",
            currentMedia: {"spotify":"https://open.spotify.com/embed/track/4vsoWZcvtvSsE0OiVvDDvX?si=e0c947796466427","youtube":"https://www.youtube.com/embed/Uz1Jwyxd4tE"}
        }
    },
    mounted () {
        console.log("PROPS")
        console.log(this.type)
        console.log(this.media)
        console.log(this.$route.params)
        axios.get("http://localhost:8000/api/getInfo")
        .then((response) => {
            this.info = response.data
        })
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
  