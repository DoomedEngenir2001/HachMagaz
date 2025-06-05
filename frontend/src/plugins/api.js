import axios from "axios";
const instance = axios.create({ // создаем instance с установленными настройками
    baseURL: "http://localhost:8000/",
    withCredentials: false,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
});
export default{
    async getProducts(index){
        return instance.get("/get_product_cards",{
            params: {"index": index}}
        );
    },
    async getAllProducts(){
        return instance.get("/get_all_product_cards");
    },
    async createOrder(user_id, prod, count, addr, method, bill, token){
        return instance.post("/newOrder", {
            headers:{
                "Authorization": `Bearer ${token}`
            },
            data: {
                "user_id": user_id,
                "address": addr,
                "method": method,
                "bill": bill,
                "productCard_ids": prod,
                "count": count
            }
        })
    },
    async SignIn(login, password){
        return instance.post("/login",{
            "login": login,
            "password":password 
        });
    },
    async SignUp(login, password, email, phone){
        return instance.post("/registration",{
            "login": login,
            "password":password,
            "email": email,
            "phone": phone
        });
    },
    async getOrders(user_id, token){
        return instance.get("/getOrders",{
            params:{"user_id":user_id},
            headers:{
                "Authorization": `Bearer ${token}`
            }
        });
    },

    async getAdress(login, token){
        return instance.post("/getAddresses",{
            "login": login,
            headers:{
                Authorization: `Bearer ${token}`
            }
        });
    },
    async getProductDict(){
        return instance.get("/getDict");
    },
    async getCart(login, token){
        return instance.post("/getCart",{
            "login": login,
            headers:{
                Authorization: `Bearer ${token}`
            }
        });
    },
    async addToCart(login, count, price, product, token){
        return instance.post("/addToCart",  {
            "login": login,
            "count":count,
            "price":price,
            "product":product
            },
            {
                headers:{
                    Authorization: `Bearer ${token}`
                }
            }
        );
    },
    async addProduct(title, desc, price, image, limit, token){
        return instance.post("/addCard", {
            "product": title,
            "description":desc,
            "price":price,
            "image":image,
            "limit": limit
            },
            {
                headers:{
                    Authorization: `Bearer ${token}`
                }
            });
    },
    async editCard(title, desc, price, image, limit, token){
               return instance.post("/editCard", {
            "id": id,
            "product": title,
            "description":desc,
            "price":price,
            "image":image,
            "limit": limit
            },
            {
                headers:{
                    Authorization: `Bearer ${token}`
                }
            }); 
    }
}