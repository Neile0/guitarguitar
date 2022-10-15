<template> 
    <div>
        <h1>What Do You Like</h1>
        <div @click="go('shape')" id="rectangle1">
          <!--<a target="_blank" href="guitar.png">-->
            <img :src="require('@/assets/guitar.png')" alt="guitar" width="200" height="400">
          <!--</a>-->
        </div>
        <div @click="go('shape')" id="rectangle2">
          <img :src="require('@/assets/guitar.png')" alt="guitar" width="200" height="400">
        </div>
        <div @click="go('shape')" id="rectangle3"></div>
        
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
      console.log(this.$route.params)
    },
    methods: {
        go(t) {
            this.$router.push({name:'resultsscreen',params:{"type":t,"media":this.media}})
        },
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
  