import { createStore } from "vuex";
import api from "../plugins/api";
export default createStore({
    state: {
        products: null,
        cart: [],
        login: null,
        address: ''
    },
    getters: {
        getProductsfromState(state){
            return state.products;
        },
        getCart(state){
            return state.cart;
        },
        getLenghtCart(state){
            let counts = 0;
            state.cart.forEach(element => {
                counts+=element.count;
            });
            return counts;
        },
        getCartCost(state){
            let sum = 0
            state.cart.forEach(element => {
                sum+=element.count*element.price;
            });
            return sum;
        },
        getLogin(state){
            return state.login;
        },
        getAddress(state){
            return state.address;
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
            console.log(name)
        state.cart.forEach((element, index) => {
                if (element.product == name)state.cart[index].count +=1;
            });
            
        },
        minusCountByName(state, name){
            state.cart.forEach((element, index) => {
                if (element.product == name)state.cart[index].count -=1;
            });
        },
        deleteItemByName(state, name){
            state.cart.forEach((element, index) => {
                if (element.product == name)state.cart.splice(index,1);
            });  
        },
        setLogin(state, name){
            state.login=name;
        },
        setAddress(state, addr){
            state.address=addr;
        }
    },
    actions: {
        async getProductsfromServer(context){
            const response = await api.getProducts();
            context.commit("setProducts", response.data);
        }
    }
})