<script setup lang="ts">
import { create, NButton, NInput } from "naive-ui";
import type StateInputInterface from '../../../share/interfaces/inputs.ts'
import type PutUserPropsPersonalCabinetRequest from '../../../share/api/PersonalCabinet/api'
import handler_put_user_props from '../../../share/handlers/PersonalCabinetHandlers'
import { ElNotification } from 'element-plus';
import { ref } from "vue";



const props = defineProps<{
  name: string
  value: string
}>()


let stateInput = ref<StateInputInterface>({
  input: '',
  active: false,
  value: props.value
});

async function pressButtonEvent(name: string, value: string, id_user: number) {
  if (stateInput.value.active) {
    try {
      const data: PutUserPropsPersonalCabinetRequest = {
        type_props: name,
        value: stateInput.value.value,
        id_user: id_user,
      };
      const res = await handler_put_user_props(data)
      stateInput.value.active = false
      return ElNotification({
        title: 'Успешно',
        message: 'Данные изменены',
        type: 'success',
        duration: 5000,
        position: 'bottom-right',
      });
    } catch (error) {
      stateInput.value.value = props.value
      stateInput.value.active = false
      // TODO Как ьбудто можно вынести отдельно и вызывать в разынх местах приложения, а не по компонентно
      return ElNotification({
        title: 'Ошибка',
        message: error.message,
        type: 'error',
        duration: 5000,
        position: 'bottom-right',
      })
    }
  } else {
    stateInput.value.active = true;
  }
}
</script>

<template>
  <div class="flex flex-row w-2/3">
    <div class="w-1/12">
      {{ name }}
    </div>
    <n-input class="w-4/6 mr-2" autosize v-model:value="stateInput.value"
      @keyup.enter="pressButtonEvent(name, stateInput.value, 10)" :placeholder="value" :disabled="!stateInput.active" />
    <n-button 
    class="w-1/6 opacity-80" 
    :type="stateInput.active == true ? 'success' : 'warning'" 
    @click="pressButtonEvent(name, stateInput.value, 10)">
      <template #icon v-if="stateInput.active == false">
        <!-- TODO EBANAYA ZAPUPA SUKA BLYAT  -->
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512">
          <path
            d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4L.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3l262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3l-31.1-31.1L51.7 376H88v48z"
            fill="currentColor"></path>
        </svg>
      </template>
      <template #icon v-if="stateInput.active == true">
        <!-- TODO EBANAYA ZAPUPA SUKA BLYAT  -->
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 24 24">
          <path d="M9 16.2L4.8 12l-1.4 1.4L9 19L21 7l-1.4-1.4L9 16.2z" fill="currentColor"></path>
        </svg>
      </template>
    </n-button>
  </div>
</template>
