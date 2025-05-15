import { createApp } from 'vue'
import App from './App.vue'
import  router  from './router';
import store from './store'
import { createYmaps } from 'vue-yandex-maps';
import './style.css'
const app = createApp(App);
app.use(router)
.use(store)
.use(createYmaps({
  // TODO в .env перенести
    apikey: '1f637575-4259-4ea8-a74e-2755ea4647df',
  }))
.mount('#app');
