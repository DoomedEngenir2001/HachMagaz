<template>
    <div @scroll="this.onScroll(event)" class = "main-page">
        <HeaderPage @contact="toContact()"
            @LogIn="toLK()" @OpenCart="this.cartIsVisible=true"></HeaderPage>
        <div class="center-align">
        <div class="product-panel">
           <productCard  class="md:w-[150px] md:h-[200px]" @showModal="showModalWindow" v-for="product in this.getProductsfromState" :key="product.product" 
           :product="product.product" :price="product.price" :imagePath="product.image" :id="product.id"
           :description="product.description"></productCard> 
        </div>
        </div>
        <!-- <div class="modal" v-show="isVisible">
            <ProductCardModal @closeModal="this.isVisible=false"    
            :product="selectedProduct" :price="selectedPrice" :description="selectedDesc"
            :imagePath="selectedImg"/>
        </div> -->
        <div  v-show="this.cartIsVisible" class="cart-modal">
            <CartModal @toMap="openMap" @closeCart="this.cartIsVisible=false"></CartModal>
        </div>
        <signInForm @exit="this.authResult()" 
        @toSignUp="this.signInIsVisble=false;this.signUpIsVisble=true;" @closeFormSignIn="this.signInIsVisble=false;this.signUpIsVisble=false;" 
        v-show="this.signInIsVisble"></signInForm>
        <signUpForm @toSignIn="this.signInIsVisble=true;this.signUpIsVisble=false;" @closeFormSignUp="this.signInIsVisble=false;this.signUpIsVisble=false;" 
        v-show="this.signUpIsVisble"></signUpForm>
        <ContactModal v-if="showContact" @closeContact="toContact()"></ContactModal>
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
import ContactModal from '../components/ContactModal.vue';
import { ElNotification } from 'element-plus';
import { onMounted } from 'vue';
export default{
    async created(){
        if (this.getProductsfromState.length ==0){
            await this.getProductsfromServer(this.getIndex);
        }
    },
    mounted() {
        document.onscrollend = async () => {
            if (!this.getEnd){
                await this.getProductsfromServer(this.getIndex);
            }else{
                return;
            }
        }
 },
    components:{
        HeaderPage,
        productCard,
        ProductCardModal,
        CartModal,
        signInForm,
        signUpForm,
        ElNotification,
        ContactModal
    },
    data(){
        return {
            // isVisible: false,
            selectedPrice: null,
            selectedProduct: null,
            selectedDesc: null,
            selectedImg: null,
            cartIsVisible: false,
            signInIsVisble: false,
            signUpIsVisble: false,
            productIsEnd: false,
            authOK: false,
            showContact: false
        }
    },
    computed: {
        ...mapGetters({
            getProductsfromState: "getProductsfromState",
            getToken: "getToken",
            getProductsfromState: "getProductsfromState",
            getIndex: "getIndex",
            getEnd: "getEnd",
            getUserId: "getUserId"  
        })
    },
    methods:{
        ...mapActions({
            getProductsfromServer: "getProductsfromServer",
            getOrders: "getOrders"
        }),
        // showModalWindow(product, price, imagePath, description){
        //     this.selectedProduct=product;
        //     this.selectedPrice=price;
        //     this.selectedDesc=description;
        //     this.selectedImg=imagePath;
        //     this.isVisible=true;
        // },
        toSignUp(){
           this.signUpIsVisble = true;
           this.signInIsVisble = false;
        },
        toSignIn(){
           this.signUpIsVisble = false;
           this.signInIsVisble = true;
        },
        authResult(){
            this.signUpIsVisble = false;
           this.signInIsVisble = false;
           console.log(this.getUserId)
           if (this.getUserId != null){
            return ElNotification({
                title: 'Успешно',
                message: 'Вход выполнен',
                type: 'success',
                duration: 5000,
                position: 'bottom-right',
            });
           }else {
            return ElNotification({
                title: 'Ошибка',
                message: 'Вход не выполнен',
                type: 'error',
                duration: 5000,
                position: 'bottom-right',
            });
           }
        },
        toLK(){
            if(this.getToken != '')this.$router.push('/personalCabinet');
            else this.toSignUp();
        },
        openMap(){
            this.$router.push('/orderMap');
        },
        toContact(){
            if(this.showContact) this.showContact = false;
            else this.showContact = true;
        }
    } 
}
</script>
<style scoped>
.main-page{
    display: flex;
    flex-direction: column;
    width: 100%;
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
    gap: 1%;
}
@media(max-width: 768px){
    .product-panel{
    grid-template-columns: repeat(2, 1fr);
    width: 95%;   
    margin-top: 20px;
    gap: 1%;
}
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