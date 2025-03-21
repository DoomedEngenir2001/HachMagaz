<template>
<div class="header">
    <img class="logo-placeholder" :src="require('@/assets/logotip.png')"/>
    <navBtn>Пицца</navBtn>
    <navBtn>Cамса</navBtn>
    <navBtn>Пиво</navBtn>
    <orangeBtn class="or-btn">Корзина</orangeBtn>
    <orangeBtn class="or-btn">Личный кабинет</orangeBtn>
</div>
</template>
<script>
import orangeBtn from './orangeBtn.vue';
import navBtn from './navBtn.vue';
export default{
components:{
    orangeBtn,
    navBtn
}
}
</script>
<style scoped>
.header{
    display: flex;
    flex-direction: row;
    align-items:center;
    height: 100px;
    /* padding: 6px 15px 10px 15px; */
    box-shadow:  5px 5px rgb(182, 182, 182);
}
.logo-placeholder{
    width: 84px;
    height: 84px;
    background-image: url(~@/assets/logo.png);
}
.or-btn{
    margin-right: 2.5%;
}
</style>