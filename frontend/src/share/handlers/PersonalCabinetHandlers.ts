// PersonalCabinetHandlers.ts
import put_user_props, { PutUserPropsPersonalCabinetRequest } from '../api/PersonalCabinet/api';

async function handler_put_user_props(data: PutUserPropsPersonalCabinetRequest) {
    const response = await put_user_props(data)
    if (response.status != 200) throw new Error(response.response.data.detail)
    else return response
    
}

export default handler_put_user_props