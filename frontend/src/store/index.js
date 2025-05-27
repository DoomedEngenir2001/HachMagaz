import { createStore } from "vuex";
import api from "../plugins/api";
import {saveStorage, getStorage} from "../plugins/persistent"
export default createStore({
    state: {
        products:  getStorage("products") || [],
        queryProducts: getStorage("products") || [],
      //  productMap: new Map(),
        cart: getStorage("cart") || [],
        orders:  getStorage("orders") || [],
        addresses: getStorage("orders") || [],
        login:  '',
        password: '',
        names: new Set(),
        email: getStorage("email") || '',
        address: getStorage("address") || '',
        name: getStorage("name") || '',
        surname: getStorage("surname") || '',
        phone: getStorage("phone") ||'',
        token: getStorage("token") ||'',
        user_id: getStorage("user_id") ||null,
        index:0,
        end: false
    },
    getters: {
        getCartIdxs(state){
            let pr_idxs = []
            state.cart.forEach(el =>{
                pr_idxs.push(el.id)
            });
            return pr_idxs;
        },
        getCartCount(state){
            let pr_cnt = []
            state.cart.forEach(el =>{
                pr_cnt.push(el.count)
            });
            return pr_cnt;
        },
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
        getProductFromOrders(state){
            let CardProducts = new Map();
            state.orders.forEach((el) =>{
                let products_ = [];
                el.Products.forEach((pr)=>{
                    state.products.forEach((product) =>{
                        if (product.id ==pr)products_.push(product); // add pr cart to arr
                    })
                    
                })
                CardProducts.set(el.Id,products_);
            });
            return CardProducts; // return map ID-> product cards
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

        getEmail(state){
            return state.email;
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
        },
        getUserId(state){
            return state.user_id;
        },
        getIndex(state){
            return state.index;
        },
        getEnd(state){
            return state.end;
        },
        getQueryProducts(state){
            return state.queryProducts;
        }
    },
    mutations:{
        setProducts(state, products_){
            products_.forEach(el =>{
                state.products.push(el)
            })
            saveStorage("products", products_);
        },
        addToCart(state, item){
            if (state.names.has(item.product) == false){
                state.names.add(item.product)
                state.cart.push(item);}            
            saveStorage("cart", state.cart);
        },
        addCountByName(state, name){
            console.log(name)
        state.cart.forEach((element, index) => {
                if (element.product == name)state.cart[index].count +=1;
            });
            saveStorage("cart", state.cart);
        },
        minusCountByName(state, name){
            state.cart.forEach((element, index) => {
                if (element.product == name && state.cart[index].count > 1)
                    state.cart[index].count -=1;
            });
            saveStorage("cart", state.cart);
        },
        deleteItemByName(state, name){
            state.names.delete(name)
            state.cart.forEach((element, index) => {
                if (element.product == name)state.cart.splice(index,1);
            });  
            saveStorage("cart", state.cart);
        },
        setCart(state, c_){
            state.cart = c_;
            saveStorage("cart", c_);
        },
        setLogin(state, name){ // cookie
            state.login=name;
            saveStorage("login", name);
        },
        setPassword(state, p_){ // cookie
            state.password= p_;
            saveStorage("password", p_);
        },
        setAddress(state, addr){ // cookie
            state.address=addr;
            saveStorage("address", addr);
           
        },
        setAddresses(state, addrs){
            state.addresses = addrs;
            saveStorage("addresses", addrs);
        },
        setName(state, n_){
            state.name = n_;
            saveStorage("name", n_);
        },
        setSurname(state, s_){
            state.surname = s_;
            saveStorage("surname", s_);
        },
        setPhone(state, p_){ // cookie
            state.phone = p_;
            saveStorage("phone", p_);
        },
        setToken(state, t_){ // cookie
            state.token = t_;
            saveStorage("token", t_);
        },
        setOrders(state, o_){ 
            state.orders = o_;
            saveStorage("orders", o_);
        },
        addProdCart(state, key, val){
            state.productMap.set(key, val);
        },
        setEmail(state, e_){ // cookie
            state.email = e_;
            saveStorage("email", e_);
        },
        setUserId(state, i){ // cookie
            state.user_id = i;
            saveStorage("user_id", i);
        },
        increment(state){
            state.index+=8;
        }, 
        setEnd(state){
            state.end=true;
        },
        setQueryProducts(state, q_){
            state.queryProducts = q_;
        }
    },
    actions: {
        async getProductsfromServer(context, index){
            const response = await api.getProducts(index);
            if (response.data[0] === "Products is ended"){
                context.commit("setEnd");
            }
            if(!context.state.end){
                context.commit("increment");
                context.commit("setProducts", response.data);
            }

        },
        async getAllProductCards(context){
            const response = await api.getAllProducts();
            context.commit("setProducts", response.data);
        },
        async createOrder(context){
            const response=await api.createOrder(context.getters.getUserId, context.getters.getCartIdxs,
                context.getters.getCartCount, context.getters.getAddress);
        },
        async SignIn(context){
            const response = await api.SignIn(context.state.login, context.state.password);
            context.commit("setToken", response.data.token);
            context.commit("setUserId", response.data.user_id);
        },
        async SignUp(context){
            const response = await api.SignUp(context.state.login, context.state.password, 
                context.state.email, context.state.phone);
            context.commit("setToken", response.data.token);
        },
        async getOrders(context){
            const response = await api.getOrders(context.state.login, context.state.token);
            context.commit("setOrders", response.data);
        },
        async getAdresses(context){
            const response = await api.getAdress(context.state.login, context.state.token);
            context.commit("setAddresses", response.data);
        },
        async getCart(context){
            const response = await api.getCart(context.state.login, context.state.token);
            context.commit("setCart", response.data);
        },
        async addToCart(context, count, price, product){
            const response = await api.addToCart(context.state.login, context.state.password,
                count, product, context.state.token);
        },
        getProductCardOnInput(context, query){
            let queryProducts =[]
            context.state.products.forEach( (el) => {
                if(el.product.indexOf(query)===0 | el.product.toLowerCase().indexOf(query)===0){
                    queryProducts.push(el);
                }
            });
            if(queryProducts.length == 0){
                context.commit('setQueryProducts', context.state.products)
            }else {
                context.commit('setQueryProducts', queryProducts);
            }
            
        }
    }
})