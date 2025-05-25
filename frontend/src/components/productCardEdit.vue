<template>
<div class="cart-item">
    <div class="central-content">
            <img :src="$attrs.image" alt="image" class="product-image"/>
        <div style="width: 90%; display: flex; flex-direction: row;">
        <div class="w-8/10 h-full flex flex-col">
            <p>{{$attrs.name}}</p>
            <p style="font-size: 18px;color: gray">{{$attrs.description}}</p>
        </div>
        <div class="footer toRight">
            <p >{{ $attrs.price }} рублей</p>   
            <orangeBtnTS @click="$emit('editCard')" class="green-bg">Изменить</orangeBtnTS>
        </div>
        </div>
    </div>
</div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import orangeBtnTS from './orangeBtnTS.vue';

interface productProps{
    image: string
    name: string
    description: string
    price: number
    id: number
}
export default defineComponent({
    setup() {

    },
    components:{
        orangeBtnTS
    }
})

</script>
<style scoped>
.cart-item{
    margin-top: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 5px;
    border-radius: 15px;
    width: 90%;
    height: 160px;
    border: solid 1px gray;
    border-radius: 20px;
    background-color: white;
    display: flex;
    flex-direction: column;
}
.central-content{
    display: flex;
    flex-direction: row;
    font-size: 28px;
    font-weight: bold;
    width: 100%;
    height: 100%;
    padding-left: 5px;
}
.product-image{
    width: 150px;
    height: 150px;
    object-fit: fill;
    background-size:contain;
}
.toRight{
    margin-right: 0;
    margin-left: auto;
}
.footer{
    display: flex;
    flex-direction: column;
    align-items: center;
    vertical-align: middle;
    margin-top: 30px;
}
.green-bg{
    background-color: #84BC59;
    color:black;
    border: solid black 1px;
    font-weight: bold;
}
</style>