<template>
<div class="flex flex-row w-32% md:2-100%">
<div style="height:100%;">
    <cancelBtn style="margin-top: 50vh; width: 40px; height: 40px; 
    border-radius: 40px;margin-right: 5px;" @click="close"></cancelBtn> 
</div>
<div class="cart">
    <div class="header-cart">
        <div>{{ countItems }} товаров на {{ this.getCartCost }} рублей</div>
    </div>
    <div class="cart-panel">
        <CartItem v-for="item in this.getCart"
        :count="item.count" :name="item.product"
        :image-path="item.imagePath" :price="item.price" :key="item.product" 
        :desc="item.description"></CartItem>
    </div>
    <div class="cart-footer">
        <div class="price">
            <div>Сумма заказа </div>
            <div style="margin-right: 25px; margin-left: auto;">{{ this.getCartCost }} рублей</div>
        </div>
        <orangeBtn @click="toCart" class="bigBtn">Заказать</orangeBtn>
    </div>
</div>
</div>

</template>
<script>
import orangeBtn from './orangeBtn.vue';
import cancelBtn from './cancelBtn.vue';
import CartItem from './CartItem.vue';
import { mapActions, mapGetters } from 'vuex';
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
        ...mapActions({
            createOrder: "createOrder"
        }),
        close(){
            this.$emit('closeCart');
        },
        async toCart(){
            this.$emit('toMap');
        }
    }
}
</script>
<style>
.cart{
    display: flex;
    flex-direction: column;
    width: 98%;
    height: 100%;
    background-color: #F3F3F7;

}
.header-cart{
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 60px;
    font-size: 36px;
    font-weight: bold;
    margin-left: 10px;
}
@media(max-width: 768px){
    .header-cart{
        font-size: 18px;
    }
}
.cart-panel{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 80%;
    font-weight: bold;
    overflow-y:scroll;
}
.cart-footer{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 10%;
    margin-left: 10px;
    font-weight: bold;
}
.to-Right{
    margin-left: auto;
    margin-right: 25px;
    background-color: #F3F3F7;
}
.price{
    display: flex;
    flex-direction: row;
    font-size: 24px;
}
.bigBtn{
    margin-top: 5px;
    width: 95%;
}
</style>
