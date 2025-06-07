/* eslint no-use-before-define: 0 */
/*прокинь в пропсы айди */
<template>
<div class="product-card">
    <div class="image-placeholder">
        <img :src="this.$props.imagePath" alt="image" 
        class="product-image" @click="showModal">
    </div>
    <div class="product-name ">{{this.$props.product}}</div>
    <div class="price-holder ">
        <div>{{this.$props.price}} руб.</div>
        <orangeBtn @click="addItemToCart" class="toRightCorner"><p class="md:visible text-2xl">+</p></orangeBtn>
    </div>
</div>
</template>
<script>
import orangeBtn from './orangeBtn.vue';
import { mapMutations } from 'vuex';
export default{
    components:{
        orangeBtn
    },
    props:{
        product: {
            required: true,
            type: String
        },
        price: {
            required: true,
            type: Number
        },
        imagePath:{
            required: true,
            type: String
        },
        description:{
            required: true,
            type: String
        },
        id: {
            requird: true,
            type: String
        }
    }, 
    methods:{
        ...mapMutations({
            addToCart: "addToCart"
        }),
        addItemToCart(){
            this.addToCart({
                "product": this.$props.product,
                "price": this.$props.price,
                "count": 1,
                "imagePath": this.$props.imagePath,
                "id": this.$props.id,
                "description" : this.$props.description
            });
        },
        showModal(){
            this.$emit("showModal", this.$props.product, this.$props.price,
            this.$props.imagePath, this.$props.description);
        }
    }
}
</script>
<style scoped>
.product-card{
    width: 100%;
    height: 500px;
    /* margin-right: 42.5px; */
    display: flex;
    flex-direction: column;
    border: 5px solid rgba( 128,128,128, 0.4);
    border-radius: 10px;
    /* box-shadow:  5px 5px rgb(175, 175, 175); */
}
@media (max-width: 768px){
    .product-card{
    width: 150px;
    height:290px;
    /* margin-right: 42.5px; */
    display: flex;
    flex-direction: column;
    border: 2px solid rgba( 128,128,128, 0.4);
    border-radius: 10px;
    /* box-shadow:  5px 5px rgb(175, 175, 175); */
}
}
    .image-placeholder{
    width: 100%;
    height: 357px;
    display: flex;
    background-image: url("../assets/phone.png");
    
    }
@media (max-width: 768px){
    .image-placeholder{
    width: 150px;
    height: 180px;
    display: flex;
    background-image: url("../assets/phone.png");
    
    }
}
.product-image{
    width: 100%;
    height: 355px;
    display: flex;
    object-fit: contain;
}
@media (max-width: 768px){
.product-image{
    width: 150px;
    height: 180px;
    display: flex;
    object-fit: contain;
}
}
.product-name{
    height: wrap;
    padding-left: 5px ;
    font-size: 36px;
    font-weight: bold;
}
@media (max-width: 768px){
.product-name{
    font-size: 16px;
}
}
.price-holder{
    height: wrap;
    display: flex;
    flex-direction: row;
    padding-left: 5px ;
    padding-right: 5px;
    font-size: 32px;
}
@media (max-width: 768px){
.price-holder{
    font-size: 18px;
}
}
.toRightCorner{
    margin-left: auto; 
    margin-right: 0;
}
@media (max-width: 768px){
.toRightCorner{
    margin-left: auto; 
    margin-right: 0;
    min-width: 50px;

}
}
</style>