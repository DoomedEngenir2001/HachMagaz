// TODO вынести api/baseURL в .env
import axios from "axios";
const url: string = 'http://localhost:8000/'


const api = axios.create({
    baseURL: url,
    withCredentials: false,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
});

export interface PutUserPropsPersonalCabinetRequest{
    type_props: string,
    value: string,
    id_user: number
}

async function put_user_props(data: PutUserPropsPersonalCabinetRequest) {
    try {
        const response = await api.patch('/user', data)
        return response.data
    } catch (error) {
        return error
    }
}
export default put_user_props