<template>
<div class="app">
<router></router>
<mainPage></mainPage>
</div>  
</template>

<script>
import mainPage from './pages/mainPage.vue';
export default {
  name: 'App',
  components: {
    mainPage
  }
}
</script>

<style>
.app {
font-family: Instrument Sans;
}
</style>
