<template>
<div class="header">
    <img class="logo-placeholder" src="../assets/logotip.png"/>
    <p class="text-3xl font-bold ml-[10px]">Панель администратора</p>
    <div class="btnContainer">
        <orangeBtnTS  @click="$emit('LogIn');" class="or-btn">Личный кабинет</orangeBtnTS>
    </div>
</div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import orangeBtnTS from './orangeBtnTS.vue';
export default defineComponent({
    setup(ctx, props){

    },
    components:{
        orangeBtnTS
    }
})
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