<template>
<div class="app">
<keep-alive>
  <router-view/>
</keep-alive>
<!-- <orderMapPage></orderMapPage> -->
</div>  
</template>

<script>
import mainPage from './pages/mainPage.vue';
import orderMapPage from './pages/orderMapPage.vue';
export default {
  name: 'App',
  components: {
    mainPage,
    orderMapPage
  }
}
</script>

<style>
.app {
font-family: Instrument Sans;
}
</style>
