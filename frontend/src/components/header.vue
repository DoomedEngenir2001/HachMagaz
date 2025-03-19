<template>
<div class="header">
    <div class="logo-placeholder"></div>
    <navBtn>Пицца</navBtn>
    <navBtn>Cамса</navBtn>
    <navBtn>Пиво</navBtn>
    <orangeBtn>Корзина</orangeBtn>
    <orangeBtn>Личный кабинет</orangeBtn>
</div>
</template>
<script>
import orangeBtn from './orangeBtn.vue';
import navBtn from './navBtn.vue';
import NavBtn from './navBtn.vue';
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
    padding: 6px 15px 10px 15px;
    box-shadow:  5px 5px rgb(114, 114, 114);
}
.logo-placeholder{
    background-image: url(~@/assets/Логотип.png);
}
</style>