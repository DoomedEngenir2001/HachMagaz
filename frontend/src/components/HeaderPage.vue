<template>
<div class="header">
    <img class="logo-placeholder" src="../assets/logotip.png"/>
    <navBtn>Пицца</navBtn>
    <navBtn>Cамса</navBtn>
    <navBtn>Пиво</navBtn>
    <div class="btnContainer">
        <orangeBtn @click="openCart" class="or-btn">Корзина</orangeBtn>
        <orangeBtn  @click="signIn" class="or-btn">Личный кабинет</orangeBtn>
    </div>
</div>
</template>
<script>
import orangeBtn from './orangeBtn.vue';
import navBtn from './navBtn.vue';
export default{
components:{
    orangeBtn,
    navBtn
},
methods:{
    openCart(){
        this.$emit('OpenCart');
    },
    signIn(){
        this.$emit('LogIn');
    }
}
}
</script>
<style scoped>
.header{
    display: flex;
    flex-direction: row;
    align-items:center;
    height: 100px;
    width:100%;
    box-shadow:  5px 5px rgb(182, 182, 182);
}
.logo-placeholder{
    width: 84px;
    height: 84px;
    margin-left: 2.5%;
    background-image: url(~@/assets/logo.png);
}
.btnContainer{
    display: flex;
     flex-direction: row; 
    margin-right: 2.5%;
    margin-left: auto;
    align-items: center;
    height: 100px;
}
.or-btn{
    margin-right: 2.5%;
}
</style>