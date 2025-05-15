<script setup ="ts">
import orangeBtnTS from '../components/orangeBtnTS.vue';
import {  ref, onBeforeMount, onMounted } from 'vue';
import { useStore } from 'vuex';
// import orderContainer from '../components/orderContainer.vue';
import UserInput from '../components/PersonalCabinet/MainBlock/UserInput.vue'

const personalCabinetItems = ref({
    inputs: []
});

onMounted(() => {
    personalCabinetItems.value = {
        inputs: [
            {
                name: 'Имя',
                value: 'Имя Абобус',
            },
            {
                name: 'Фамилия',
                value: 'Фамилия Абобус',
            },
            {
                name: 'Адрес',
                value: 'Адрес Абобус',
            },
            {
                name: 'Телефон',
                value: 'Телефон Абобус',
            },
        ]
    };
});
</script>


<template>
    <div class="flex flex-col">
        <!-- TODO Как будто бы можно более глобально вынести не таскать за собой header -->
        <div class="flex flex-row w-full h-[60px] text-3xl shadow-xl">
            <div class="text-3xl font-bold pl-[20px] leading-[60px]">Личный кабинет</div>
            <orangeBtnTS @click="$router.push('/')" class="mr-[50px] ml-auto">Главная</orangeBtnTS>
        </div>

        <div class="m-5">
            <div class="flex flex-col gap-5 pt-5">
                <UserInput
                v-for="item in personalCabinetItems.inputs" :key="item"
                :name="item.name"
                :value="item.value"
                />
            </div>
        </div>
        <div class="flex flex-col w-full h-[60px] text-3xl shadow-md">
            <div class="text-3xl font-bold pl-[20px] leading-[60px]">Мои заказы</div>
            <orderContainer v-for="order in orders" :key="order" :date="order.createTime"
            :Address="order.address" :cost="order.cost" :products="productMap.get(order.id)"
            class="mt-[5px]"></orderContainer>
        </div>
    </div>

</template>
