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
    }
}