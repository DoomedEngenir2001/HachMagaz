<template>
    <div class = "main-page">
        <header></header>
        <div class="product-panel">
           <productCard v-for="product in this.getProductsfromState"></productCard> 
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters, mapMutations } from 'vuex';
import header from '@/components/header.vue';
import productCard from '@/components/productCard.vue';
export default{
    async beforeMount(){
        await this.getProductsfromServer();
    },
    components:{
        header,
        productCard
    },
    computed: {
        ...mapGetters({
            getProductsfromState: "getProductsfromState"
        })
    },
    methods:{
        ...mapActions({
            getProductsfromServer: "getProductsfromServer"
        })
    }

}
</script>
<style scoped>
.main-page{
    display: flex;
    flex-direction: column;
}
.product-panel{
    width: 100vh;
    height: wrap;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
}
</style>