<template>
    <div>
        <div class='wrapper'>
            <div class='carousel'>
                <div v-for="item in info" :key="item.skU_ID"  class='carousel__item'>
                    <div class='carousel__item-body'>
                        <div v-if="hasModel(item.skU_ID)" style="float:left;text-align:left;border:1px solid grey;padding-right:36px;width:100px;height:200px;">
                            <ThreeDModel :uri="'/models/'+item.skU_ID+'/' + item.skU_ID + '.glb'" :poster="'/models/'+item.skU_ID+'/'+'poster.webp'"/>
                        </div>
                        <div v-if="!hasModel(item.skU_ID)" id="guitarImg" style="float:left;text-align:left;border:1px solid grey;width:100px;height:200px;">
                            <img width=100 height=200 :src="item.pictureMain"/>
                        </div>
                        <div id="guitarInfo">
                          
                            <p class='title'>Make:{{item.brandName}}</p>
                            <p>Model: {{item.itemName}}</p>
                           
                        </div>                    
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
  <script>
  import ThreeDModel from './ThreeDModel.vue'
  import axios from 'axios'
  export default {
    name: 'ResultsScreen',
    components: {
      ThreeDModel
    },
    props: ['type','media'],
    data () {
        return {
            gotGuitars: false,
            info: [],
            isLoaded:false,
            currentInfo: {},
            currentMedia: {"spotify":"https://open.spotify.com/embed/track/4vsoWZcvtvSsE0OiVvDDvX?si=e0c947796466427","youtube":"https://www.youtube.com/embed/Uz1Jwyxd4tE"}
        }
    },
    mounted () {
        this.data = { "type":this.type,"media":this.media}
        axios.get("http://localhost:8000/api/3d-models")
        .then((response) => {
          this.modelGuitars = response.data
          console.log(this.modelGuitars)
        })
        axios.post("http://localhost:8000/api/media/",this.data)
        .then((response) => {
            this.info = response.data
            for (var i=0; i< 5; i++) {
              console.log(this.info[i].brandName)
            }
            this.isLoaded = true
            console.log(this.info)
            this.currentInfo = this.info[0]
            this.gotGuitars = true
        })
    },
    methods: {
        hasModel(id) {
          console.log(id)
          for (var i=0; i < this.modelGuitars.length; i++) {
            if (this.modelGuitars[i] == id) {
              return true
            }
          }
          return false
        },
        goHome() {
            this.$router.push({name:'videoscreen'})
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

  .model{
    position: relative;
    right:100px;
    top:50px;
  }

  .carousel {
    position: relative;
    top: 350px;
    left: 300px;
    width: 600px;
    display: flex;
    justify-content: center;
    flex-direction: column;
  }
  .carousel__item {
    display: flex;
    align-items: center;
    position: absolute;
    width: 100%;
    padding: 0 12px;
    opacity: 0;
    filter: drop-shadow(0 2px 2px #555);
    will-change: transform, opacity;
    -webkit-animation: carousel-animate-vertical 100s linear infinite;
            animation: carousel-animate-vertical 100s linear infinite;
  }
  
  .carousel__item:nth-child(1) {
    -webkit-animation-delay: calc(10s * -1);
            animation-delay: calc(10s * -1);
  }
  
  .carousel__item:nth-child(2) {
    -webkit-animation-delay: calc(10s * 0);
            animation-delay: calc(10s * 0);
  }
  
  .carousel__item:nth-child(3) {
    -webkit-animation-delay: calc(10s * 1);
            animation-delay: calc(10s * 1);
  }
  
  .carousel__item:nth-child(4) {
    -webkit-animation-delay: calc(10s * 2);
            animation-delay: calc(10s * 2);
  }
  
  .carousel__item:nth-child(5) {
    -webkit-animation-delay: calc(10s * 3);
            animation-delay: calc(10s * 3);
  }
  
  .carousel__item:nth-child(6) {
    -webkit-animation-delay: calc(10s * 4);
            animation-delay: calc(10s * 4);
  }
  
  .carousel__item:nth-child(7) {
    -webkit-animation-delay: calc(10s * 5);
            animation-delay: calc(10s * 5);
  }
  
  .carousel__item:nth-child(8) {
    -webkit-animation-delay: calc(10s * 6);
            animation-delay: calc(10s * 6);
  }
  
  .carousel__item:last-child {
    -webkit-animation-delay: calc(-10s * 2);
            animation-delay: calc(-10s * 2);
  }
  
  
  .carousel__item-body {
    width: 100%;
    background-color: #fff;
    border-radius: 8px;
    padding: 16px 20px 16px 70px;
    box-sizing: 100px;
  }
  
  .title {
    text-transform: uppercase;
    font-size: 20px;
    margin-top: 10px;
  }
  
  @-webkit-keyframes carousel-animate-vertical {
    0% {
      transform: translateY(100%) scale(0.5);
      opacity: 0;
      visibility: hidden;
    }
    3%, 11.1111111111% {
      transform: translateY(100%) scale(0.7);
      opacity: 0.4;
      visibility: visible;
    }
    14.1111111111%, 22.2222222222% {
      transform: translateY(0) scale(1);
      opacity: 1;
      visibility: visible;
    }
    25.2222222222%, 33.3333333333% {
      transform: translateY(-100%) scale(0.7);
      opacity: 0.4;
      visibility: visible;
    }
    36.3333333333% {
      transform: translateY(-100%) scale(0.5);
      opacity: 0;
      visibility: visible;
    }
    100% {
      transform: translateY(-100%) scale(0.5);
      opacity: 0;
      visibility: hidden;
    }
  }
  
  @keyframes carousel-animate-vertical {
    0% {
      transform: translateY(100%) scale(0.5);
      opacity: 0;
      visibility: hidden;
    }
    3%, 11.1111111111% {
      transform: translateY(100%) scale(0.7);
      opacity: 0.4;
      visibility: visible;
    }
    14.1111111111%, 22.2222222222% {
      transform: translateY(0) scale(1);
      opacity: 1;
      visibility: visible;
    }
    25.2222222222%, 33.3333333333% {
      transform: translateY(-100%) scale(0.7);
      opacity: 0.4;
      visibility: visible;
    }
    36.3333333333% {
      transform: translateY(-100%) scale(0.5);
      opacity: 0;
      visibility: visible;
    }
    100% {
      transform: translateY(-100%) scale(0.5);
      opacity: 0;
      visibility: hidden;
    }
  }
</style>


/** <div id="social">
    <Spotify :uri="currentMedia.spotify"/>
    <YouTube :uri="currentMedia.youtube"/>
</div> */
  