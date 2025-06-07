import axios from "axios";
const instance = axios.create({ // создаем instance с установленными настройками
    baseURL: "https://tiksiproducts47.ru/api/",
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
        console.log(token)
        const header = {
            headers: {"Authorization": `Bearer ${token}`}
            }
        const data = {
                "user_id": user_id,
                "address": addr,
                "method": method,
                "bill": bill,
                "productCard_ids": prod,
                "count": count
            }  
        return instance.post("/newOrder", data, header);
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
        return instance.post("/getAddresses",{"login": login},{headers:{Authorization: 
            `Bearer ${token}`}});
    },
    async addProduct(title, desc, price, image, limit, token){
        const data = {
            "product": title,
            "description":desc,
            "price":price,
            "image":image,
            "limit": limit
            }
            const headers = {headers: {"Authorization": `Bearer ${token}`}}
        return instance.post("/addCard",data ,headers);
    },
    async editCard(title, desc, price, image, limit, token){
        const data = {
            "id": id,
            "product": title,
            "description":desc,
            "price":price,
            "image":image,
            "limit": limit
        }
        const headers = {headers:{Authorization: `Bearer ${token}`}}
        return instance.post("/editCard", data, headers); 
    }
}