import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { createYmaps } from 'vue-yandex-maps'
import './style.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import naive from 'naive-ui'
const app = createApp(App)

app.use(router)
  .use(store)
  .use(ElementPlus)
  .use(naive)
  // TODO в .env перенести
  .use(createYmaps({
    apikey: '1f637575-4259-4ea8-a74e-2755ea4647df',
  })).mount('#app')