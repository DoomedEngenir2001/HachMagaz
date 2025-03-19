<template>
<div class="product-card">
    <div class="product-image"></div>
    <div class="product-name">this.$props.product</div>
    <div class="price-holder">
        <div>this.$props.price</div>
        <orangeBtn>Выбрать</orangeBtn>
    </div>
</div>
</template>
<script>
import orangeBtn from './orangeBtn.vue';
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
        }
    }
}
</script>
<style scoped>
.product-card{
    width: 380px;
    height: 500px;
    display: flex;
    flex-direction: column;
}
.product-image{
    width: 357px;
    height: 357px;
}
.product-name{
    height: wrap;
    font-size: 24px;
}
.price-holder{
    height: wrap;
    display: flex;
    flex-direction: row;
    font-size: 40px;
}
.product-image{
    background-image: url(this.$props.imagePath);
}
</style>