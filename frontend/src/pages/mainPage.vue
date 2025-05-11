<template>
    <div class = "main-page">
        <HeaderPage @LogIn="toLK()" @OpenCart="this.cartIsVisible=true"></HeaderPage>
        <div class="center-align">
        <div class="product-panel">
           <productCard @showModal="showModalWindow" v-for="product in this.getProductsfromState" :key="product.product" 
           :product="product.product" :price="product.price" :imagePath="product.image" :id="product.id"
           :description="product.description"></productCard> 
        </div>
        </div>
        <div class="modal" v-show="isVisible">
            <ProductCardModal @closeModal="this.isVisible=false"    
            :product="selectedProduct" :price="selectedPrice" :description="selectedDesc"
            :imagePath="selectedImg"/>
        </div>
        <div  v-show="this.cartIsVisible" class="cart-modal">
            <CartModal @toMap="openMap" @closeCart="this.cartIsVisible=false"></CartModal>
        </div>
        <signInForm @toSignUp="this.signInIsVisble=false;this.signUpIsVisble=true;" @closeFormSignIn="this.signInIsVisble=false;this.signUpIsVisble=false;" 
        v-show="this.signInIsVisble"></signInForm>
        <signUpForm @toSignIn="this.signInIsVisble=true;this.signUpIsVisble=false;" @closeFormSignUp="this.signInIsVisble=false;this.signUpIsVisble=false;" 
        v-show="this.signUpIsVisble"></signUpForm>
    </div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import productCard from '../components/productCard.vue';
import HeaderPage from '../components/HeaderPage.vue';
import ProductCardModal from '../components/ProductCardModal.vue';
import CartModal from '../components/CartModal.vue';
import signInForm from '../components/signInForm.vue';
import signUpForm from '../components/signUpForm.vue';
export default{
    async created(){
        if (this.getProductsfromState.length ==0){
            await this.getProductsfromServer();
 //           await this.getOrders();
        }
    },
    components:{
        HeaderPage,
        productCard,
        ProductCardModal,
        CartModal,
        signInForm,
        signUpForm
    },
    data(){
        return {
            isVisible: false,
            selectedPrice: null,
            selectedProduct: null,
            selectedDesc: null,
            selectedImg: null,
            cartIsVisible: false,
            signInIsVisble: false,
            signUpIsVisble: false
        }
    },
    computed: {
        ...mapGetters({
            getProductsfromState: "getProductsfromState",
            getToken: "getToken",
            getProductsfromState: "getProductsfromState"
        })
    },
    methods:{
        ...mapActions({
            getProductsfromServer: "getProductsfromServer",
            getOrders: "getOrders"
        }),
        showModalWindow(product, price, imagePath, description){
            this.selectedProduct=product;
            this.selectedPrice=price;
            this.selectedDesc=description;
            this.selectedImg=imagePath;
            this.isVisible=true;
        },
        toSignUp(){
           this.signUpIsVisble = true;
           this.signInIsVisble = false;
        },
        toSignIn(){
           this.signUpIsVisble = false;
           this.signInIsVisble = true;
        },
        toLK(){
            if(this.getToken != '')this/this.$router.push('/personalCabinet');
            else toSignUp();
        },
        openMap(){
            this.$router.push('/orderMap');
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
    width: 90%;
    align-items: center;
    height: wrap;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
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