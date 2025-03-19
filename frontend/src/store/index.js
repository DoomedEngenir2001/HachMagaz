import { createStore } from "vuex";
import api from '@/plugins/api';
export default createStore({
    state: {
        products: null
    },
    getters: {
        getProductsfromState(state){
            return state.products;
        }
    },
    mutations:{
        setProducts(state, products_){
            state.products = products_;
        }
    },
    actions: {
        async getProductsfromServer(context){
            const response = await api.getProducts();
            context.commit("setProducts", response.data);
        }
    }
})