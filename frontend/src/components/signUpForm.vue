<template>
    <div class="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center ">
        <div class="flex-column items-center w-wrap h-wrap bg-white rounded-3xl p-[8px]">
            <div class="flex-row w-full h-2/10">
                <cancelBtn @click="this.$emit('closeFormSignUp');" class="m-r-0 m-l-auto"></cancelBtn>
            </div>
            <div class="h-[105px] w-full text-4xl leading-[105px] text-center font-bold">Регистрация</div>
            <div class="h-[30px] w-full mt-[5px] text-base leading-[30px] font-bold">Телефон</div>
            <input v-model="this.login" placeholder="Введите логин" class="outline w-[630px] h-[75px] mt-[5px] rounded-3xl">
            <div class="h-[30px] w-full mt-[5px] text-base leading-[30px] font-bold">Пароль</div>
            <input v-model="this.password" placeholder="Введите пароль" class="outline w-[630px] h-[75px] mt-[5px] rounded-3xl">
            <div class="h-[30px] w-full mt-[5px] text-base leading-[30px] font-bold">Email</div>
            <input v-model="this.email" placeholder="Введите пароль" class="outline w-[630px] h-[75px] mt-[5px] rounded-3xl">
            <div class="h-[30px] w-full mt-[5px] text-base leading-[30px] font-bold">Телефон</div>
            <input v-model="this.phone" placeholder="Введите пароль" class="outline w-[630px] h-[75px] mt-[5px] rounded-3xl">
            <div class="mt-[10px] flex text-center text-gray text-xl underline" @click="this.$emit('toSignIn');">Войти</div>
            <div class="mt-[65px] flex w-full text-center justify-center"><orangeBtn  @click="signUp()" class="text-white w-[220px] ">Зарегистрироваться</orangeBtn></div>    
            
        </div>
    </div>
    </template>
    <script>
    /// ВАЛИДАЦИИ !!!
    import { mapActions, mapMutations } from "vuex";
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
                password: "",
                email: "",
                phone: ""
            }
        },
        methods:{
            ...mapActions({
                SignUp: "SignUp"
            }),
            ...mapMutations({
                setEmail: "setEmail",
                setPhone: "setPhone",
                setLogin: "setLogin",
                setPasword: "setPassword"
            }),
            async signUp(){
                this.setEmail(this.email);
                this.setPhone(this.phone);
                this.setLogin(this.login);
                this.setPasword(this.password);
                await this.SignUp();
                this.$emit('closeFormSignUp');
            }
        }
    }
    </script>
    