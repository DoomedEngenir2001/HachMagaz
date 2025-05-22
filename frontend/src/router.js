import { createRouter,createWebHistory } from 'vue-router'
import App from './App.vue';
import OrderMapPage from './pages/orderMapPage.vue';
import MainPage from './pages/mainPage.vue';
import orderPage from './pages/orderPage.vue';
import PersonalCabinet from './pages/PersonalCabinet.vue';
import adminPage from './pages/adminPage.vue'
const routes = [
    {path: '/', component: MainPage},
    {path: '/orderMap', component: OrderMapPage},
    {path: '/order', component: orderPage},
    {path: '/personalCabinet', component: PersonalCabinet},
    {path: '/adminPage', component: adminPage}
];

const router = createRouter({routes, history: createWebHistory()});
export default  router;