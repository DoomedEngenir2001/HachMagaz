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
        requiresAuth: false
    }},
    {path: '/orderMap', component: OrderMapPage, meta:{
        requiresAuth: true
    }},
    {path: '/order', component: orderPage, meta:{
        requiresAuth: true
    }},
    {path: '/personalCabinet', component: PersonalCabinet, meta:{
        requiresAuth: true
    }},
    {path: '/error404', component: error404, meta:{
        requiresAuth: false
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
    } else{
        next();
    }
    if (to.path != '/' && to.path!= '/orderMap' && to.path!='/order' 
        && to.path!= '/personalCabinet'){
        next('/error404');
    }
})
export default  router;