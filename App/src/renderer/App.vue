<template>
  <div id="app">
     <MainPanel/>
  </div>
</template>

<script>
import MainPanel from './components/MainPanel.vue'

export default {
  name: 'app',
  components: {
    MainPanel
  }
}
</script>

<style>
 #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

body{
  min-width: 400px!important;
  margin-left: 0;
  margin-right: 0
}
</style>
