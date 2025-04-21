<template>
<div class="cart-item">
    <div class="central-content">
        <img :src="props.imagePath" class="product-image"/>
        <div>{{props.name}}</div>
        <div class="toRight">{{ cost }} рублей</div>
    </div>
</div>
</template>
<script setup lang="ts">
import { computed } from 'vue';
const props = defineProps<{
    imagePath: string
    name: string
    price: number
    count: number
}>()
    const cost = computed(() => {
        return props.price * props.count;
    })
</script>
<style scoped>
.cart-item{
    margin-top: 5px;
    margin-left: 5px;
    width: 98%;
    height: 230px;
    background-color: white;
    display: flex;
    flex-direction: column;
}
.central-content{
    color: black;
    line-height: 140px;
    display: flex;
    flex-direction: row;
    font-size: 24px;
    width: 100%;
    height: 140px;
    padding-left: 5px;
}
.product-image{
    width: 140px;
    height: 140px;
    background-size:contain;
}
.toRight{
    margin-right: 5px;
    margin-left: auto;
}
.footer{
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 20px;
    width: 100%;
    height: 60px;
}
</style>