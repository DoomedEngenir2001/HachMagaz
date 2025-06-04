<template>
  <div class="flex flex-col">
    <!-- Header -->
    <div class="flex flex-row w-full h-[60px] shadow-xl items-center">
      <div class="md:text-3xl text-xl
       font-bold pl-[20px] leading-[60px]">Личный кабинет</div>
      <orangeBtnTS @click="$router.push('/')" class="md:min-w-[100px] h-[40px] md:h-[50px] 
      mr-[50px] ml-auto">Главная</orangeBtnTS>
    </div>

    <!-- User info -->
    <div class="m-5">
      <div class="flex flex-col gap-5 pt-5">
        <UserInput
          v-for="item in personalCabinetItems.inputs"
          :key="item.name"
          :name="item.name"
          :value="item.value"
          @save-input="saveInput"
        />
      </div>
    </div>

    <!-- Orders section -->
    <div class="hidden md:flex flex-col w-full text-3xl shadow-md" >
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
import { useStore } from 'vuex'

const store = useStore();
const personalCabinetItems = ref({
  inputs: [] as Array<{name: string, value: string}>
})
const saveInput = (name:string, value:string) =>{
  if(name == 'Имя'){
    store.commit("setName", value);
  }
  else if (name == 'Фамилия'){
    store.commit("setSurname", value);
  }
  else if (name == 'Адрес'){
    store.commit("setAddress", value);
  }else if (name == 'Телефон'){
    store.commit("setPhone",value );
  }
}

onMounted(() => {
  personalCabinetItems.value = {
    inputs: [
      { name: 'Имя', value: store.getters.getName },
      { name: 'Фамилия', value: store.getters.getSurname },
      { name: 'Адрес', value: store.getters.getAddress },
      { name: 'Телефон', value: store.getters.getPhone }
    ]
  }
})
</script>