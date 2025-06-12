import { createRouter,createWebHistory } from 'vue-router'
import App from './App.vue';
import OrderMapPage from './pages/orderMapPage.vue';
import MainPage from './pages/mainPage.vue';
import orderPage from './pages/orderPage.vue';
import PersonalCabinet from './pages/PersonalCabinet.vue';
import adminPage from './pages/adminPage.vue'
import {getStorage} from "./plugins/persistent"
const routes = [
    {path: '/', component: MainPage},
    {path: '/orderMap', component: OrderMapPage, meta:{
        requiresAuth: true
    }},
    {path: '/order', component: orderPage, meta:{
        requiresAuth: true
    }},
    {path: '/personalCabinet', component: PersonalCabinet, meta:{
        requiresAuth: true
    }}
];
const router = createRouter({routes, history: createWebHistory()});
router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth){
        const token = getStorage("token");
        if (token != ''){
            next()
        }else{
            next('/');
        }
    } else{
        next();
    }
})
export default  router;