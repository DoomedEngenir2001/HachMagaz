<template>
<div class="product-card-modal">
    <div class="header"><cancelBtn @click="$emit('closeModal')"/></div>
    <div class="product-image">
        <img :src="this.$props.imagePath" class="image-placeholder"/>
    </div>
    <div class="name">{{this.$props.product}}</div>
    <div class="description">{{this.$props.description}}</div>
    <div class="footer">
        <div>{{this.$props.price}} рублей</div>
        <orangeBtn class="alignToRight" @click="addtoCart">Выбрать</orangeBtn>
    </div>
</div>
</template>
<script>
import cancelBtn from './cancelBtn.vue';
import orangeBtn from './orangeBtn.vue';
import { mapMutations } from 'vuex';
export default{
    components:{
        cancelBtn, 
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
        }
    },
    methods:{
        ...mapMutations({
            addToCart: "addToCart"
        }),
        addtoCart(){
            this.addToCart({
                "product": this.$props.product,
                "price": this.$props.price,
                "count": 1,
                "imagePath": this.$props.imagePath
            });
           this.$emit("closeModal");
        }
    }
}
</script>
<style scoped>
.product-card-modal{
    width: 620px;
    height: 500px;
    display: flex;
    background-color: #ffffff;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    border-radius: 25px;
}
.header{
    padding-top: 10px;
    padding-right: 15px;
    display: flex;
    flex-direction: row;
    width: 620px;
    height: 40px;
}
.product-image{
    height:300px;
    width: 300px;
    align-items: center;

}
.image-placeholder{
    width: 300px;
    height: 300px;
}
.name{
    width: 620px;
    height: 40px;
    font-size:36px;
    padding-left: 15px;
    text-align: left;
}
.description{
    height: 180px;
    width: 620px;
    padding-left: 15px;
    font-size:20px;
    text-align: justify;
}
.footer{
    display: flex;
    flex-direction: row;
    width: 90%;
    padding-left: 5px ;
    padding-right: 5px;
    font-size: 40px;
}
.alignToRight{
    margin-left: auto;
    margin-right: 5px;
    margin-bottom: 5px;
}
</style>