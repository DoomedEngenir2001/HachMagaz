// PersonalCabinetHandlers.ts
import put_user_props from '../api/PersonalCabinet/api';
import type PutUserPropsPersonalCabinetRequest from '../api/PersonalCabinet/api'

async function handler_put_user_props(data: PutUserPropsPersonalCabinetRequest) {
    try {
        const response = await put_user_props(data);
        return response;
    } catch (error) {
        if (error instanceof Error) {
            alert(`Ошибка при обновлении данных: ${error.message}`);
        } else {
            alert('Произошла неизвестная ошибка');
        }
        throw error;
    }
}

export default handler_put_user_props