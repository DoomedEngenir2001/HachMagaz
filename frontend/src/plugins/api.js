import axios from "axios";
const instance = axios.create({ // создаем instance с установленными настройками
    baseURL: "http://localhost:3000/",
    withCredentials: false,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
});
export default{
    async getProducts(){
        return instance.get("/getProductCards");
    },
    async createOrder(name, surname, phone, addr, cost,status, prod){
        return instance.post("/newOrder", {
            "Name" : name,
            "Surname" : surname,
            "Adress" : addr,
            "Phone" : phone,
            "Cost" : cost,
            "Status" : status,
            "Products" :prod
            
        })
    },
    async SignIn(login, password){
        return instance.post("/login",{
            "login": login,
            "password":password 
        });
    },
    async SignUp(login, password){
        return instance.post("/registration",{
            "login": login,
            "password":password 
        });
    },
    async getOrders(login, token){
        return instance.post("/getOrders",{
            "login": login
        },
        {
            headers:{
                Authorization: `Bearer ${token}`
            }
        });
    },

    async getAdress(login, token){
        return instance.post("/getAddresses",{
            "login": login
        },
        {
            headers:{
                Authorization: `Bearer ${token}`
            }
        });
    },
    async getCart(login, token){
        return instance.post("/getCart",{
            "login": login
        },
        {
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
    }

}