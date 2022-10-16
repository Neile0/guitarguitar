<template> 
<div>
  <link href="stylesheet.css" rel="stylesheet"> 
    <div>
      <p style="color:white;">What Do You Like</p>
    </div>
    <div class="AllButtons" style="width: 90%;margin-left 5%">
      <div id="rectangle1">
      <div class="image-stack">
        <div class="image-stack__item image-stack__item--topguitar">
          <img  @click="go('shape')" :src="require('@/assets/guitar.png')" alt="guitar" width="100" height="300">
        </div>
        <div class="image-stack__item image-stack__item--bottomguitar">
          <img  @click="go('shape')" :src="require('@/assets/guitar2.png')" alt="guitar" width="100" height="300">
        </div>
      </div>
      <b>Looks</b>
    </div>
    <div id="rectangle2">
      <div class="image-stack">
        <div class="image-stack__item image-stack__item--toppick">
          <img  @click="go('shape')" :src="require('@/assets/pick-up.png')" alt="pick-up" width="150" height="200">
        </div>
        <div class="image-stack__item image-stack__item--bottompick">
          <img  @click="go('shape')" :src="require('@/assets/pick-up2.png')" alt="pick-up" width="150" height="200">
        </div>
      </div>
      <b>Sound</b>
    </div>
    <div @click="go('brand')" id="rectangle3">
      <img  :src="require('@/assets/gibson.png')" alt="guitar" width="200" height="95">
      <img  :src="require('@/assets/fender.png')" alt="guitar" width="200" height="95">
      <img  :src="require('@/assets/martin.png')" alt="guitar" width="200" height="80">
      <b>Brand</b>
    </div>
    </div>
   
    </div>
</template>
<script>

export default {
  name: 'WhatDoYouLike',
  components: {

  },
  props: ['media'],
  data () {
      return {
          
      }
  },
  mounted () {
    
  },
  methods: {
      changemyVar() {
          this.myVar ="https://open.spotify.com/embed/track/1Ud6moTC0KyXMq1Oxfien0?si=c565fd4210664132"
      },
      go(t) {
          this.$router.push({name:'resultsscreen',params:{"type":t,"media":this.media}})
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
  p{
    font-size: 50px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    font-family: 'Courier New', Courier, monospace;
    color: rgb(0, 0, 0)
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
    font-size: 50px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    font-family: 'Courier New', Courier, monospace;
    color: rgb(0, 0, 0);
    border-radius: 25px;
    background: #767676;
    opacity: 0.5;
    padding: 20px;
    width: 200px;
    height: 400px;
    margin-left: 33%;
    margin-right: 3%;
    float: left;

  }
  #rectangle2{
    font-size: 50px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    font-family: 'Courier New', Courier, monospace;
    color: rgb(0, 0, 0);
    border-radius: 25px;
    background: #767676;
    opacity: 0.5;
    padding: 20px;
    width: 200px;
    height: 400px;
    margin-left: 3%;
    margin-right: 3%;
    float: left;
    
  }
  #rectangle3{
    font-size: 50px;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    font-family: 'Courier New', Courier, monospace;
    color: rgb(0, 0, 0);
    border-radius: 25px;
    background: #767676;
    opacity: 0.5;
    padding: 20px;
    width: 200px;
    height: 400px;
    margin-left: 3%;
    margin-right: 3%;
    float: left;
  }
  #rectangle1:hover{
    background-color: black;
    transition: 0.3s;
    color: white;
  }
  #rectangle2:hover{
    background-color: black;
    transition: 0.3s;
    color: white;
  }
  #rectangle3:hover{
    background-color: black;
    transition: 0.3s;
    color: white;
  }
  .image-stack {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    position: relative;
  }
  .image-stack__item--topguitar {
      z-index: 2;
      position: relative;
      left: 0px;
      padding: 0px 60px 0px 50px;
    }
  .image-stack__item--topguitar:hover{
    opacity: 0;
  }
    .image-stack__item--bottomguitar {
      position: absolute;
      left: 50px;
      z-index:1;
  }

  .image-stack__item--toppick {
      z-index: 2;
      position: relative;
      left: 0px;
      top: 0px;
      padding: 60px 40px 40px 30px;
    }
  .image-stack__item--toppick:hover{
    opacity: 0;
  }
    .image-stack__item--bottompick {
      position: absolute;
      left: 30px;
      top: 60px;
      z-index:1;
  }
  </style>
  