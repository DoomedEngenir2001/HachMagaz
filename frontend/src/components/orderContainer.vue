<template>
    <div class="flex flex-col w-full h-wrap items-center">
        <div @click = "show = show == false ? true : false;$forceUpdate();" 
        class="w-96/100 items-center h-[65px] text-white text-2xl 
        flex flex-row bg-[#ff6900]">
            <div class="w-2/10 h-full leading-[65px] text-white text-xl">{{ props.date}}</div>
            <div class="w-6/10 h-full leading-[65px] text-white text-xl">{{ props.Address}}</div>
            <div class="w-2/10 h-full leading-[65px] text-white text-xl">{{ props.cost}} рублей</div>
        </div>
        <div v-if="show" class="w-full h-wrap text-white text-xl">
            <OrderItem  v-for="product in props.products" :key="product.id" 
            :name="product.product" :price="product.price" :imagePath="product.imagePath"
            :count="1"
            class="w-full h-wrap"></OrderItem>
        </div>
    </div>
</template>
<script setup lang="ts">
import OrderItem from './OrderItem.vue';
interface productCard {
        product: string,
        price:  number,
        description : string,
        imagePath: string,
        id: number
}
    const props = defineProps<{
        date: string
        Address: string
        cost: number,
        products: Array<productCard>
    }>();
    var show = false;
</script>