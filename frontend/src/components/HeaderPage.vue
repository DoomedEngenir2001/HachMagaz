<template>
<div class="header md:h-[50px]">
    <img class="logo-placeholder" src="../assets/logotip.png"/>
    <div class="media-title text-4xl font-bold ml-[30px]">ХачМагаз</div>
    <div class="btnContainer">
        <orangeBtn class="or-btn flex items-center 
        min-w-[50px] justify-center"
        @click="showContact"><img width="30px" height="30px" src="../assets/telephone.png"></orangeBtn>
        <orangeBtn @click="openCart" class="or-btn flex items-center 
        min-w-[50px] justify-center"><img  width="30px" height="30px" src="../assets/shopping-cart.png"></orangeBtn>
        <orangeBtn class=" or-btn flex justify-center items-center" @click="signIn"><img class="w-[30px] h-[30px] " src="../assets/user.png"></orangeBtn>
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
data(){
    return {
        media: false
    }
},
methods:{
    mediaHandler(){
        if(this.media==false)this.media = true;
        else this.media = false;
    },
    openCart(){
        this.$emit('OpenCart');
    },
    signIn(){
        this.$emit('LogIn');
    },
    showContact(){
        this.$emit('contact');
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
@media (max-width: 768px) {
    .header{
        display: flex;
        flex-direction: row;
        align-items:center;
        height: 80px;
        width:100%;
        font-size: 20px;
    }
}
@media (max-width: 768px) {
    .media-title{
    display: none;
    }
}
.logo-placeholder{
    width: 84px;
    height: 84px;
    margin-left: 2.5%;
    background-image: url(~@/assets/logo.png);
}
@media (max-width: 768px) {
    .logo-placeholder{
    width: 50px;
    height: 50px;
    margin-left: 2.5%;
    background-image: url(~@/assets/logo.png);
}
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
@media (max-width: 768px) {
    .or-btn{
        min-width: 50px;
        width: 50px;
        height: 50px;
        margin-right: 2.5%;
    }
}
</style>