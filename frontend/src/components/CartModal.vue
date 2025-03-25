<template>
<div class="cart">
    <div class="header-cart">
        <div>{{ countItems }} товаров на {{ this.getCartCost }} рублей</div>
        <cancelBtn class="toRight" @click="close"></cancelBtn> 
    </div>

    <div class="cart-panel">
        <CartItem v-for="item in this.getCart"
        :count="item.count" :name="item.product"
        :image-path="item.imagePath" :price="item.price" :key="item.product"></CartItem>
    </div>
    <div class="cart-footer">
        <div class="price">Сумма заказа {{ this.getCartCost }} рублей</div>
        <orangeBtn class="bigBtn">Заказать</orangeBtn>
    </div>
</div>
</template>
<script>
import { initFlowbite } from 'flowbite'
import orangeBtn from './orangeBtn.vue';
import cancelBtn from './cancelBtn.vue';
import CartItem from './CartItem.vue';
import { mapGetters } from 'vuex';
export default{
    components:{
        orangeBtn,
        cancelBtn,
        CartItem
    },
    
// initialize components based on data attribute selectors
    onMounted(){
    initFlowbite();
},

    computed:{
        ...mapGetters({
            getLenghtCart: 'getLenghtCart',
            getCart : 'getCart',
            getCartCost : 'getCartCost'
         }),
        countItems(){
            return this.getLenghtCart;
        },
        cost(){
            return this.getCartCost;
        }

    },
    methods:{
        close(){
            this.$emit('closeCart');
        }
    }
}
</script>
<style>
.cart{
    display: flex;
    flex-direction: column;
    width: 40%;
    height: 100%;
    background-color: #F3F3F7;
    padding: 5px 5px 5px 5px;
}
.header-cart{
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 60px;
    font-size: 36px;
}
.cart-panel{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 80%;
}
.cart-footer{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 10%;
}
.to-Right{
    margin-left: auto;
    margin-right: 20px;
}
.price{
    font-size: 24px;
}
.bigBtn{
    margin-top: 5px;
    width: 95%;
}
</style>
