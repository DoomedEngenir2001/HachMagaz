<template>
<div class="flex flex-col">
    <div class="flex flex-row w-full h-[60px] text-3xl flex shadow-xl">
        <div class="text-3xl font-bold pl-[20px] leading-[60px]">Личный кабинет</div>
        <orangeBtnTS @click="$router.push('/')" class="mr-[50px] ml-auto">Главная</orangeBtnTS>
    </div>
    <div class="flex flex-col w-2/5 mt-[40px] ml-[20px]">
        <div class="flex flex-row h-[40px]">
            <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Имя</div>
            <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="name" :placeholder="name" class="w-[285px] h-[40px]"></input></div>
            <div class="w-[40px] h-[40px] bg-[url('../assets/pencil.png')]"></div>
        </div>
        <div class="flex flex-row h-[40px] mt-[40px]">
            <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Фамилия</div>
            <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="surname" :placeholder="surname"  class="w-[285px] h-[40px]"></input></div>
            <div class="w-[40px] h-[40px] bg-[url('../assets/pencil.png')]"></div>
        </div>
        <div class="flex flex-row h-[40px] mt-[40px]">
            <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Адрес</div>
            <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="address" :placeholder="address" class="w-[285px] h-[40px]"></input></div>
            <div class="w-[40px] h-[40px] bg-[url('../assets/pencil.png')]"></div>
        </div>
        <div class="flex flex-row h-[40px] mt-[40px]">
            <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Телефон</div>
            <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="phone" :placeholder="phone" class="w-[285px] h-[40px]"></input></div>
            <div class="w-[40px] h-[40px] bg-[url('../assets/pencil.png')]"></div>
        </div>
    </div>
    <div class="flex flex-col w-full h-[60px] text-3xl flex  shadow-md">
        <div class="text-3xl font-bold pl-[20px] leading-[60px]">Мои заказы</div>
        <orderContainer v-for="order in orders" :date="order.date" 
        :Address="order.Adress" :cost="order.Cost" :products="productMap.get(order.Id)"
        class="mt-[5px]"></orderContainer>
    </div>
</div>
</template>
<script lang="ts">
import orangeBtnTS from '../components/orangeBtnTS.vue';
import {  ref, onBeforeMount } from 'vue';
import { useStore } from 'vuex';
import orderContainer from '../components/orderContainer.vue';
export default{
    setup(){
        const store = useStore();
        const orders = store.getters.getOrders; 
        const productMap = store.getters.getProductFromOrders;
        console.log(productMap);
        const surname = ref(`${store.getters.getSurname}`);
        const name = ref(`${store.getters.getName}`);
        const address = ref(`${store.getters.getAddress}`);
        const phone = ref(`${store.getters.getPhone}`);
       return {
            surname, name, address, phone, orders, productMap
        }
    },
    components: {
        orangeBtnTS,
        orderContainer
    }
}
</script>