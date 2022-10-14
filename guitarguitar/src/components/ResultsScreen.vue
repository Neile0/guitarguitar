<template>
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
            
            <Spotify :uri="myVar"/>
            <YouTube/>
        </div>
    </div>
</template>
  
  <script>
  import Spotify from './Spotify.vue'
  import YouTube from './YouTube.vue'
  export default {
    name: 'ResultsScreen',
    components: {
      Spotify,
      YouTube
    },
    props: {
      msg: String
    },
    data () {
        return {
            make: "Fender",
            model: "Stratocaster",
            guitarists: "Eric Clapton",
            myVar: "https://open.spotify.com/embed/track/4vsoWZcvtvSsE0OiVvDDvX?si=e0c947796466427"
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
  