<template> 
    <div>
        <div :v-for="x in myList">
            <p></p>
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
              myList: ["a","b","c"]
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
        font-weight: 20px;
        font-family: 'Courier New', Courier, monospace;
        color: black
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
        font-size: 10px;
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
      