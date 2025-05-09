import { createStore } from "vuex";
import api from "../plugins/api";
export default createStore({
    state: {
        products:  [],
      //  productMap: new Map(),
        cart: [],
        orders: [],
        addresses: [],
        login: '',
        password: '',
        email: '',
        address: 'Полюстровский проспект',
        name: 'Test',
        surname: 'Test',
        phone: '8-999-999-99-99',
        token: '',
        user_id: null
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
                if (element.product == name && state.cart[index].count > 0)
                    state.cart[index].count -=1;
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
        },
        addProdCart(state, key, val){
            state.productMap.set(key, val);
        },
        setEmail(state, e_){
            state.email = e_;
        },
        setUserId(state, i){
            state.user_id = i;
        }
    },
    actions: {
        async getProductsfromServer(context){
            const response = await api.getProducts();
        //    response.data.forEach((el)=> {
        //        context.commit("addProdCart", el.id, new Object(el));
        //    });
            context.commit("setProducts", response.data);
        },
        async createOrder(context){
            const response=await api.createOrder(context.getters.getUserId, context.getters.getCartIdxs,
                context.getters.getCartCount);
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
        }
    }
})