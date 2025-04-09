<template>
<div class="w-full h-full flex flex-col">
    <div class="w-full h-[60px] text-3xl flex shadow-xl leading-[60px] pl-[10px] font-bold">
        Оформление заказа
    </div>
    <div class="w-full h-full flex flex-row mt-[41px] p-[10px]">
        <div class="text-base w-3/5">

        <div class=" h-full text-base">
            <div class="w-full h-[40px] flex flex-row">
                <div class="w-[90px] h-[40px] text-xl font-bold leading-[40px]">Имя</div>
                <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input v-model="name" class="w-[285px] h-[40px]"></input></div>
            </div>
            <div class="w-full h-[40px] flex flex-row mt-[21px]">
                <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Фамилия</div>
                <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="surname" class="w-[285px] h-[40px]"></input></div>
            </div>
            <div class="w-full h-[40px] flex flex-row mt-[21px]">
                <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Телефон</div>
                <div class="w-[285px] h-[40px] rounded-md border mr-0 ml-auto"><input  v-model="phone" class="w-[285px] h-[40px]"></input></div>
            </div>
            <div class="w-full h-[40px] flex flex-row mt-[21px]">
                <div class="w-[100px] h-[40px] text-xl font-bold leading-[40px]">Адрес</div>
                <div class="flex w-[285px] h-[40px] text-xl font-bold rounded-xl">{{ addrr }}</div>
            </div>
        </div>

        <div class="flex-col flex ml-[11px] mr-auto">
            <div class="w-full h-[40px] font-bold text-2xl">Cпособ оплаты</div>
            <div class="w-full h-[40px] flex flex-row"><input  type="radio" value="SBP" name="buying"/><img class="w-[40px] h-[40px] object-scale-down flex ml-[10px]" src="../assets/sbp.png"/><div class="flex leading-[40px] text-xl font-bold pl-[6px]">Система Быстрых платежей</div></div>
            <div class="w-full h-[40px] flex flex-row"><input  type="radio" value="Card" name="buying"/><img class="w-[40px] h-[40px] object-scale-down flex ml-[10px]" src="../assets/credit-card.png"/><div class="flex leading-[40px] text-xl font-bold pl-[6px]">Картой на сайте</div></div>
            <div class="w-[230px] h-[75px]">
                <input v-model="card" placeholder="Номер карты" class="w-[227px] h-[25px] rounded-md border mt-[10px]"/>
                <div class="flex-row mt-[18px]">
                    <input v-model="srok" placeholder="Срок действия" class="w-[139px] h-[25px] mt-[10px] rounded-md border"/>
                    <input v-model="cvv" placeholder="CVV" class="w-[80px] h-[25px] ml-[10px] rounded-md border"/>
                </div>
            </div>
            <div class="w-full h-[40px] mt-[20px] flex flex-row"><input type="radio" value="Nal" name="buying"/><img class="w-[40px] h-[40px] object-scale-down flex ml-[10px]" src="../assets/money.png"/><div class="flex leading-[40px] text-xl font-bold pl-[6px]">Наличными</div></div>        
        </div>
        <orangeBtnTS class="bg-white text-black mt-[20px]" @click="cancelOrder">Отменить заказ</orangeBtnTS>
        </div>
        <div class="w-2/5 h-full flex flex-col text-base pl-[40px] pr-[40px]">
            <div class="w-full text-3xl font-bold">Cостав заказа</div>
            <div class="flex-row flex text-xl font-bold w-full h-[30px]" v-for="item in cart"><div class="flex h-[30px]">{{item.product}}</div><div class="flex mr-0 ml-auto h-[30px]">{{item.price}} рублей</div></div>
            <div class="flex-row flex text-xl font-bold"><div>Сумма заказа</div><div class="mr-0 ml-auto">{{ cost }} рублей</div></div>
            <orangeBtnTS class="mt-[20px]" @click="makeOrder">Оформить заказ</orangeBtnTS>
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
        
        const cancelOrder = () =>{
            router.push('/');
        }

        const makeOrder = async () =>{
            const resp = await store.actions.postProductsToServer(name, surname, phone);
            router.push('/');
        }

        return {
            cart, cost, addrr, name, surname, card, srok,cvv, cancelOrder, makeOrder
        }
    },
    components:{
        orangeBtnTS
    }
}
</script>