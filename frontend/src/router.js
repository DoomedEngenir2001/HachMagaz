import { createRouter,createWebHistory } from 'vue-router'
import App from './App.vue';
import OrderMapPage from './pages/orderMapPage.vue';
import MainPage from './pages/mainPage.vue';
import orderPage from './pages/orderPage.vue'
const routes = [
    {path: '/', component: MainPage},
    {path: '/orderMap', component: OrderMapPage},
    {path: '/order', component: orderPage}
];

const router = createRouter({routes, history: createWebHistory()});
export default  router;