/* eslint no-use-before-define: 0 */
/*прокинь в пропсы айди */
<template>
<div class="product-card">
    <div class="image-placeholder">
        <img :src="this.$props.imagePath" alt="image" class="product-image" @click="showModal">
    </div>
    <div class="product-name">{{this.$props.product}}</div>
    <div class="price-holder">
        <div>{{this.$props.price}} рублей</div>
        <orangeBtn @click="addItemToCart" class="toRightCorner">Выбрать</orangeBtn>
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
    width: wrap;
    height: 500px;
    /* margin-right: 42.5px; */
    display: flex;
    flex-direction: column;
    box-shadow:  5px 5px rgb(175, 175, 175);
}
.image-placeholder{
    width: 357px;
    height: 357px;
    
}
.product-image{
    max-width: 355px;
    max-height: 355px;

}
.product-name{
    height: wrap;
    padding-left: 5px ;
    font-size: 32px;
    font-weight: bold;
}
.price-holder{
    height: wrap;
    display: flex;
    flex-direction: row;
    padding-left: 5px ;
    padding-right: 5px;
    font-size: 40px;
}
.product-image{
    width: 357px;
    height: 357px;
    object-fit: contain;
}
.toRightCorner{
    margin-left: auto; 
    margin-right: 0;
}
</style>