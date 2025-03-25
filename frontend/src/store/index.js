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
        },
        getLenghtCart(state){
            return state.cart.length;
        },
        getCartCost(state){
            let sum = 0
            state.cart.forEach(element => {
                sum+=element.count*element.price;
            });
            return sum;
        }
    },
    mutations:{
        setProducts(state, products_){
            state.products = products_;
        },
        addToCart(state, item){
            state.cart.push(item);
        },
        addCountByName(state, name){
            this.state.cart.forEach((element, index) => {
                if (element.product == name)this.state.cart[index].count +=1;
            });
            
        },
        minusCountByName(state, name){
            this.state.cart.forEach((element, index) => {
                if (element.product == name)this.state.cart[index].count -=1;
            });
        },
        deleteItemByName(state, name){
            this.state.cart.forEach((element, index) => {
                if (element.product == name)this.state.cart.splice(index,1);
            });
            
        }
    },
    actions: {
        async getProductsfromServer(context){
            const response = await api.getProducts();
            context.commit("setProducts", response.data);
        }
    }
})