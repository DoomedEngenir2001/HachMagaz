<template>
    <div class = "main-page">
        <HeaderPage @OpenCart="this.cartIsVisible=true"></HeaderPage>
        <div class="center-align">
        <div class="product-panel">
           <productCard @showModal="showModalWindow" v-for="product in this.getProductsfromState" :key="product.product" 
           :product="product.product" :price="product.price" :imagePath="product.imagePath"
           :description="product.description"></productCard> 
        </div>
        </div>
        <div class="modal" v-if="isVisible">
            <ProductCardModal @closeModal="this.isVisible=false"    
            :product="selectedProduct" :price="selectedPrice" :description="selectedDesc"
            :imagePath="selectedImg"/>
        </div>
        <div v-if="this.cartIsVisible" class="cart-modal">
            <CartModal @closeCart="this.cartIsVisible=false"></CartModal>
        </div>
        
    </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import productCard from '@/components/productCard.vue';
import HeaderPage from '@/components/HeaderPage.vue';
import ProductCardModal from '@/components/ProductCardModal.vue';
import CartModal from '@/components/CartModal.vue';
export default{
    async created(){
        await this.getProductsfromServer();
    },
    components:{
        HeaderPage,
        productCard,
        ProductCardModal,
        CartModal
    },
    data(){
        return {
            isVisible: false,
            selectedPrice: null,
            selectedProduct: null,
            selectedDesc: null,
            selectedImg: null,
            cartIsVisible: false
        }
    },
    computed: {
        ...mapGetters({
            getProductsfromState: "getProductsfromState"
        })
    },
    methods:{
        ...mapActions({
            getProductsfromServer: "getProductsfromServer"
        }),
        showModalWindow(product, price, imagePath, description){
            this.selectedProduct=product;
            this.selectedPrice=price;
            this.selectedDesc=description;
            this.selectedImg=imagePath;
            this.isVisible=true;
        }
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
.modal{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.cart-modal{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content:right;
}
</style>