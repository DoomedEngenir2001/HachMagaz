import { createRouter,createWebHistory } from 'vue-router'
import mainPage from '@/pages/mainPage.vue';
const routes = [
    {path: '/', component: mainPage},

];

const router = createRouter({routes, history: createWebHistory(process.env.BASE_URL)});
export { router}