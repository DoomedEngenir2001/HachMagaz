<template>
  <div class="flex flex-col">
    <!-- Header -->
    <div class="flex flex-row w-full h-[60px] text-3xl shadow-xl">
      <div class="text-3xl font-bold pl-[20px] leading-[60px]">Личный кабинет</div>
      <orangeBtnTS @click="$router.push('/')" class="mr-[50px] ml-auto">Главная</orangeBtnTS>
    </div>

    <!-- User info -->
    <div class="m-5">
      <div class="flex flex-col gap-5 pt-5">
        <UserInput
          v-for="item in personalCabinetItems.inputs"
          :key="item.name"
          :name="item.name"
          :value="item.value"
        />
      </div>
    </div>

    <!-- Orders section -->
    <div class="flex flex-col w-full text-3xl shadow-md">
      <div class="text-3xl font-bold pl-[20px] leading-[60px]">Мои заказы</div>
      <TableOrders />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import orangeBtnTS from '../components/orangeBtnTS.vue'
import UserInput from '../components/PersonalCabinet/MainBlock/UserInput.vue'
import TableOrders from '../components/PersonalCabinet/MainBlock/TableOrders.vue'

const personalCabinetItems = ref({
  inputs: [] as Array<{name: string, value: string}>
})

onMounted(() => {
  personalCabinetItems.value = {
    inputs: [
      { name: 'Имя', value: 'Имя Абобус' },
      { name: 'Фамилия', value: 'Фамилия Абобус' },
      { name: 'Адрес', value: 'Адрес Абобус' },
      { name: 'Телефон', value: 'Телефон Абобус' }
    ]
  }
})
</script>