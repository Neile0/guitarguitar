<template>
    <div>
        <div>
            <div v-if="!gotGuitars" id="loading">
  <img id="loading-image" src="https://www.surreycomet.co.uk/resources/images/10135528.jpg?type=responsive-gallery-fullscreen" alt="Loading..." />
</div>
        
            <div id="guitarImg" style="float:left;text-align:left;border:1px solid grey;width:400px;height:600px;">
                <img width=400 height=600 :src="currentInfo.pictureMain" />
            </div>
            <div style="color:white;" id="guitarInfo">
                <p>Make:{{currentInfo.brandName}}</p>
                <p>Model: {{currentInfo.itemName}}</p>
               
            </div>
            <div id="social">
              
            </div>
        </div>
    </div>
</template>
  
  <script>
 
  import axios from 'axios'
  export default {
    name: 'ResultsScreen',
    components: {
      
    },
    props: ['type','media'],
    data () {
        return {
            gotGuitars: false,
            currentInfo: {},
            currentMedia: {"spotify":"https://open.spotify.com/embed/track/4vsoWZcvtvSsE0OiVvDDvX?si=e0c947796466427","youtube":"https://www.youtube.com/embed/Uz1Jwyxd4tE"}
        }
    },
    mounted () {
        console.log("PROPS")
        console.log(this.type)
        console.log(this.media)
        console.log(this.$route.params)
        this.data = { "type":this.type,"media":this.media}
        axios.post("http://localhost:8000/api/media/",this.data)
        .then((response) => {
            this.info = response.data
            this.currentInfo = this.info[0]
            console.log(this.info)
            this.gotGuitars = true
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
    #loading {
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  opacity: 1;
  background-color: #fff;
  z-index: 99;
}

#loading-image {
  z-index: 100;
}


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
  p{
    
  }
  </style>
  