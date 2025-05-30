<template>
    <div class="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center ">
    <div class="flex-column items-center w-wrap h-wrap bg-white rounded-3xl p-[8px]">
        <div class="flex-row w-full h-1/10">
            <cancelBtn @click="$emit('close');" class="m-r-0 m-l-auto"></cancelBtn>
        </div>
        <input type="radio" v-model="paymentMethod" value="Наличными"/>
        <input type="radio" v-model="paymentMethod" value="Cистема быстрых платежей"/>
        <input type="radio" v-model="paymentMethod" value="Банковской картой"/>
        <div v-show="paymentMethod == 'Банковской картой'" class="flex flex-col text-xl">
            <div>Номер карты</div>
            <input v-model="cardNumber" placeholder="1111222233334444"/>
            <div>Годна до</div>
            <input v-model="cardNumber" placeholder="12/25"/>
            <div>CVV</div>
            <input v-model="cardNumber"/>
        </div>
        <orangeBtnTS>Оплатить</orangeBtnTS>
    </div>
</div>
</template>
<script lang="ts">
import { defineComponent, ref } from "vue";
import cancelBtnTS from "./cancelBtnTS.vue";
import orangeBtnTS from "./orangeBtnTS.vue";
export default defineComponent({
setup(){
    const paymentMethod = ref('');
    const cardNumber = ref('');
    const expireCard = ref('')
    const cvv =ref('');
    return {paymentMethod, cardNumber, expireCard, cvv}
},
components:{
    orangeBtnTS,  cancelBtnTS
}
})
</script>