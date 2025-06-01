<template>
<div class="w-full h-full fixed top-0 left-0 bg-black/50 flex items-center justify-center">
    <div class="flex flex-col items-center w-70% h-70% bg-white rounded-3xl p-[8px]">
                <div class="w-full h-[40px] flex flex-row">
                    <div class="w-[90px] h-[40px] text-xl font-bold leading-[40px]">Имя</div>
                    <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input v-model="name" class="w-[285px] h-[40px]" readonly></input></div>
                </div>
                <div class="w-full h-[40px] flex flex-row mt-[21px]">
                    <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Фамилия</div>
                    <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="surname" class="w-[285px] h-[40px]" readonly></input></div>
                </div>
                <div class="w-full h-[40px] flex flex-row mt-[21px]">
                    <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Телефон</div>
                    <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="phone" class="w-[285px] h-[40px]" readonly></input></div>
                </div>
                <div class="w-full h-wrap flex flex-row mt-[21px]">
                    <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Адрес</div>
                    <div class="flex w-wrap h-[40px] text-xl rounded-xl">{{ addrr }}</div>
                </div>
            <div class="w-full h-[40px] font-bold text-2xl">Оплата только наличными</div>   
            <div class="w-full flex flex-col text-base pl-[40px] pr-[40px]">
                <div class="w-full text-3xl font-bold">Cостав заказа</div>
                <div class="flex-row flex text-xl  w-full h-[30px]" v-for="item in cart"><div class="flex h-[30px]">{{item.product}} x{{ item.count }}</div><div class="flex mr-0 ml-auto h-[30px]">{{item.price * item.count}} рублей</div></div>
                <div class="flex-row flex text-xl font-bold"><div>Сумма заказа</div><div class="mr-0 ml-auto">{{ cost }} рублей</div></div>
                <orangeBtnTS class="mt-[20px] " @click="makeOrder">Оформить заказ</orangeBtnTS>         
                <orangeBtnTS class="bg-white text-black mt-[20px]" @click="cancelOrder">Отменить заказ</orangeBtnTS>
            </div>
    </div>
</div>
</template>
<script lang="ts">
import orangeBtnTS from '../components/orangeBtnTS.vue';
import {  ref } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';


export default {
    setup(props, ctx) {
        const store = useStore();
        const cart = store.getters.getCart;
        const addrr = ref(store.getters.getAddress);
        const cost = ref(store.getters.getCartCost);
        const name = ref(store.getters.getName);
        const surname = ref(store.getters.getSurname);
        const phone = ref(store.getters.getPhone);
        const card = ref('');
        const srok = ref('');
        const cvv = ref('');
        const router = useRouter();
        const paymentMethod = ref('')
        const cancelOrder = () =>{
            router.push('/');
        }
        const makeOrder = async () =>{
            const resp = await store.dispatch("createOrder", "Nal");
            store.commit("setCart", []);
            router.push("/")
        }
        return {
            cart, cost, addrr, name, surname, card, srok,cvv, paymentMethod, phone, cancelOrder, makeOrder
        }
    },
    components:{
        orangeBtnTS
    }
}
</script>