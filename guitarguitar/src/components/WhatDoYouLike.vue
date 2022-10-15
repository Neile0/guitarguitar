<template> 
<div>
  <link href="stylesheet.css" rel="stylesheet"> 
    <div id="rectangle1">
      <img :src="require('@/assets/guitar.png')" alt="guitar" width="150" height="400">
    </div>
    <div id="rectangle2">
      <img :src="require('@/assets/guitar.png')" alt="guitar" width="150" height="400">
    </div>
    <div id="rectangle3">
      <img :src="require('@/assets/guitar.png')" alt="guitar" width="150" height="400">
    </div>
    </div>
</template>
  
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
  