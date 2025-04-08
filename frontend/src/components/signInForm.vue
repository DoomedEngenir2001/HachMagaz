<template>
<div class="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center ">
    <div class="flex-column items-center w-wrap h-wrap bg-white rounded-3xl p-[8px]">
        <div class="flex-row w-full h-1/10">
            <cancelBtn @click="this.$emit('closeFormSignIn');" class="m-r-0 m-l-auto"></cancelBtn>
        </div>
        <div class="h-[105px] w-full text-4xl leading-[105px] text-center font-bold">Вход</div>
        <div class="h-[30px] w-full mt-[5px] text-base leading-[30px] font-bold">Телефон или эмаил</div>
        <input :login placeholder="Введите логин" class="outline w-[630px] h-[75px] mt-[5px] rounded-3xl">
        <div class="h-[30px] w-full mt-[5px] text-base leading-[30px] font-bold">Пароль</div>
        <input :password placeholder="Введите пароль" class="outline w-[630px] h-[75px] mt-[5px] rounded-3xl">
        <div class="mt-[10px] w-full flex text-center text-gray text-xl underline" @click="this.$emit('toSignUp');">Зарегистрироваться</div>
        <div class="mt-[65px] flex items-center justify-center"><orangeBtn  @click="signIn()" class="text-white w-[220px] ">Войти</orangeBtn></div>    
       
    </div>
</div>
</template>
<script>
 /// ВАЛИДАЦИИ !!!
import cancelBtn from "./cancelBtn.vue";
import orangeBtn from "./orangeBtn.vue";
export default {
    components: {
        cancelBtn,
        orangeBtn
    },
    data(){
        return{
            login: "",
            password: ""
        }
    },
    methods:{
        signIn(){
            this.$emit('closeFormSignIn');
        }
    }
}
</script>
