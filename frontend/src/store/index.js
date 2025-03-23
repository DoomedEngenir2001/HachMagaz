import { createStore } from "vuex";
import api from '@/plugins/api';
export default createStore({
    state: {
        products: null,
        cart: []
    },
    getters: {
        getProductsfromState(state){
            return state.products;
        },
        getCart(state){
            return state.cart;
        }
    },
    mutations:{
        setProducts(state, products_){
            state.products = products_;
        },
        addToCart(state, item){
            state.cart.push(item);
        }
    },
    actions: {
        async getProductsfromServer(context){
            const response = await api.getProducts();
            context.commit("setProducts", response.data);
        }
    }
})