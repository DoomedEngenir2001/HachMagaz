import { createStore } from "vuex";
import api from "../plugins/api";
export default createStore({
    state: {
        products: null,
        cart: [],
        orders: [],
        addresses: [],
        login: '',
        password: '',
        address: '',
        name: '',
        surname: '',
        phone: '',
        token: ''
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
        },
        getAddresses(state){
            return state.addresses;
        },
        getName(state){
            return state.name;
        },
        getSurname(state){
            return state.surname;
        },
        getPhone(state){
            return state.phone;
        },
        getLogin(state){
            return state.login;
        },
        getPassword(state){
            return state.password;
        },
        getPasswordSHA(state){
            return;
        },
        getToken(state){
            return state.token;
        },
        getOrders(state){
            return state.orders;
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
        setCart(state, c_){
            state.cart = c_;
        },
        setLogin(state, name){
            state.login=name;
        },
        setPassword(state, p_){
            state.password= p_;
        },
        setAddress(state, addr){
            state.address=addr;
        },
        setAddresses(state, addrs){
            state.addresses = addrs;
        },
        setName(state, n_){
            state.name = n_;
        },
        setSurname(state, s_){
            state.surname = s_;
        },
        setPhone(state, p_){
            state.phone = p_;
        },
        setToken(state, t_){
            state.token = t_;
        },
        setOrders(state, o_){
            state.orders = o_;
        }
    },
    actions: {
        async getProductsfromServer(context){
            const response = await api.getProducts();
            context.commit("setProducts", response.data);
        },
        async postProductsToServer(context, n_, s_, p_){
            context.commit("setName", n_);
            context.commit("setSurname", s_);
            context.commit("setPhone", p_);
            const response=await api.createOrder(context.state.getName, context.state.getSurname, 
                context.state.getPhone, context.state.getAddress, context.state.getCartCost,
                 'OK', context.state.getCart);
        },
        async SignIn(context){
            const response = await api.SignIn(context.state.login, context.state.password);
            context.commit("setToken", response.data.token);
        },
        async SignUp(context){
            const response = await api.SignUp(context.state.login, context.state.password);
            context.commit("setToken", response.data.token);
        },
        async getOrders(context){
            const response = await api.getOrders(context.state.login, context.state.token);
            context.commit("setOrders", response.data.orders);
        },
        async getAdresses(context){
            const response = await api.getAdress(context.state.login, context.state.token);
            context.commit("setAddresses", response.data.addresses);
        },
        async getCart(context){
            const response = await api.getCart(context.state.login, context.state.token);
            context.commit("setCart", response.data.addresses);
        },
        async addToCart(context, count, price, product){
            const response = await api.addToCart(context.state.login, context.state.password,
                count, product, context.state.token);
        }
    }
})