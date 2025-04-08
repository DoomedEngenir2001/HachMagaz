<template>
<div class="app">
<router-view/>
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
