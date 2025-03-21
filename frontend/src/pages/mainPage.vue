<template>
    <div class = "main-page">
        <HeaderPage></HeaderPage>
        <div class="center-align">
        <div class="product-panel">
           <productCard v-for="product in this.getProductsfromState" :key="product.product" 
           :product="product.product" :price="product.price" :imagePath="product.imagePath"></productCard> 
        </div>
        </div>
    </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import productCard from '@/components/productCard.vue';
import HeaderPage from '@/components/HeaderPage.vue';
export default{
    async created(){
        await this.getProductsfromServer();
    },
    components:{
        HeaderPage,
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
.center-align{
    display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.product-panel{

    margin-top:50px;
    width: wrap;
    align-items: center;
    height: wrap;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
}
</style>