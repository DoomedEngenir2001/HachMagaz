import { createRouter,createWebHistory } from 'vue-router';
import App from './App.vue';
import OrderMapPage from './pages/orderMapPage.vue';
import MainPage from './pages/mainPage.vue';
import orderPage from './pages/orderPage.vue';
import PersonalCabinet from './pages/PersonalCabinet.vue';
import error404 from './pages/error404.vue';
import adminPage from './pages/adminPage.vue';
import {getStorage} from "./plugins/persistent";
const routes = [
    {path: '/', component: MainPage, meta:{
        requiresAuth: false,
        requiresCart: false,
        requiresAdress: false
    }},
    {path: '/orderMap', component: OrderMapPage, meta:{
        requiresCart: true,
        requiresAuth: false,
        requiresAdress: false
    }},
    {path: '/order', component: orderPage, meta:{
        requiresAdress: true,
        requiresCart: false,
        requiresAuth: false
    }},
    {path: '/personalCabinet', component: PersonalCabinet, meta:{
        requiresAuth: true,
        requiresCart: false,
        requiresAdress: false
    }},
    {path: '/:pathMatch(.*)*', component: error404, meta:{
        requiresAuth: false,
        requiresCart: false,
        requiresAdress: false
    }  

    }
];
const router = createRouter({routes, history: createWebHistory()});
router.beforeEach((to, from, next) => {
    if (to.meta.requiresAuth){
        const token = getStorage("token");
        if (token && token != ''){
            next()
        }else{
            next('/');
        }
    }else if (to.meta.requiresCart){
        const cart = getStorage("cart");
        if (cart){
            next()
        }else{
            next('/')
        }
    } else if (to.meta.requiresAdress){
        const addr = getStorage("address");
        if (addr){
            next()
        }else{
            next('/')
        }
    }else  {
        next();
    }
})
export default  router;