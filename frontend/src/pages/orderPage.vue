<template>
<div class="w-full h-full flex flex-col">
    <div class="w-full h-[60px] text-3xl flex shadow-xl leading-[60px] pl-[10px] font-bold">
        Оформление заказа
    </div>
    <div class="w-full h-wrap flex flex-row mt-[41px] p-[10px]">
        <div class="text-base w-3/5">
        <div class=" h-full text-base">
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
            <div class="w-full h-fit flex flex-row mt-[21px]">
                <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Адрес</div>
                <div class="flex w-[285px] h-[40px] text-xl rounded-xl">{{ addrr }}</div>
            </div>
        </div>
        <div class="flex-col flex ml-[11px] mr-auto">
            <div class="w-full h-[40px] font-bold text-2xl">Cпособ оплаты</div>
            <!-- <div class="w-full h-[40px] flex flex-row"><input  type="radio" value="sbp" name="buying" v-model="paymentMethod"/><div class="flex leading-[40px] text-xl font-bold pl-[6px]">Система Быстрых платежей</div></div> -->
            <div class="w-full h-[40px] flex flex-row"><input  type="radio" value="bank_card" name="buying" v-model="paymentMethod"/><img class="w-[40px] h-[40px] object-scale-down flex ml-[10px]" src="../assets/credit-card.png"/><div class="flex leading-[40px] text-xl font-bold pl-[6px]">Картой на сайте</div></div>
            <div class="w-full h-[40px] mt-[20px] flex flex-row"><input type="radio" value="Nal" name="buying" v-model="paymentMethod"/><img class="w-[40px] h-[40px] object-scale-down flex ml-[10px]" src="../assets/money.png"/><div class="flex leading-[40px] text-xl font-bold pl-[6px]">Наличными</div></div>        
        </div>
        <orangeBtnTS class="bg-white text-black mt-[20px]" @click="cancelOrder">Отменить заказ</orangeBtnTS>
        </div>
        <div class="w-2/5 h-full flex flex-col text-base pl-[40px] pr-[40px]">
            <div class="w-full text-3xl font-bold">Cостав заказа</div>
            <div class="flex-row flex text-xl  w-full h-[30px]" v-for="item in cart"><div class="flex h-[30px]">{{item.product}} x{{ item.count }}</div><div class="flex mr-0 ml-auto h-[30px]">{{item.price * item.count}} рублей</div></div>
            <div class="flex-row flex text-xl font-bold"><div>Сумма заказа</div><div class="mr-0 ml-auto">{{ cost }} рублей</div></div>
            <orangeBtnTS class="mt-[20px] " @click="makeOrder">Оформить заказ</orangeBtnTS>
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
            // payment
            
            const resp = await store.dispatch("createOrder", paymentMethod.value);
           window.location.replace(resp.data.url)
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