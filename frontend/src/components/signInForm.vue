<template>
<div class="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center ">
    <div class="flex-column items-center md:w-90% lg:w-wrap h-wrap bg-white rounded-3xl p-[8px]">
        <div class="flex-row w-full h-1/10">
            <cancelBtn @click="this.$emit('closeFormSignIn');" class="m-r-0 m-l-auto"></cancelBtn>
        </div>
        <div class="h-[105px] w-full text-4xl leading-[105px] text-center font-bold">Вход</div>
        <div class="h-[30px] w-full mt-[5px] text-xl leading-[30px] font-bold">Логин</div>
        <input v-model="this.login" placeholder="Введите логин" class="outline lg:w-[630px] lg:h-[75px] mt-[5px] rounded-3xl 
        md:w-[310px] md:h-[50px]">
        <span v-if="this.submitted && !this.loginIsValid" 
        class="flex text-base text-red-600">Это поле должно быть заполнено!</span>
        <div class="h-[30px] w-full mt-[5px] text-xl leading-[30px] font-bold">Пароль</div>
        <input v-model="this.password" type="password" placeholder="Введите пароль" class="outline lg:w-[630px] lg:h-[75px] mt-[5px] 
        rounded-3xl md:w-[310px] md:h-[50px]">
        <span v-if="this.submitted && !this.passwordIsValid" 
        class="flex text-base text-red-600">Это поле должно быть заполнено!</span>
        <div class="mt-[20px] w-full flex text-center text-gray text-xl justify-center"><orangeBtn class="text-white w-[220px] " @click="this.$emit('toSignUp');">Зарегистрироваться</orangeBtn></div>
        <div class="mt-[20px] w-full flex items-center justify-center"><orangeBtn  @click="signIn()" class="text-white w-[220px] ">Войти</orangeBtn></div>    
    </div>
</div>
</template>
<script>
import { mapActions, mapMutations } from "vuex";
import cancelBtn from "./cancelBtn.vue";
import orangeBtn from "./orangeBtn.vue";
import { sha256, sha224 } from 'js-sha256';
export default {
    components: {
        cancelBtn,
        orangeBtn
    },
    data(){
        return{
            login: "",
            password: "",
            submitted: false
        }
    },
    computed:{
            passwordIsValid(){
                if (this.password.length > 5) return true;
                else return false;
            },
            loginIsValid(){
                if (this.login !=="") return true;
                else return false;
            },
            isFormValid(){
                this.submitted = true;
                return this.loginIsValid && this.passwordIsValid
            },
            passwordHash(){
                return sha256(this.password)
            }
    },
    methods:{
        ...mapActions({
            SignInAction: "SignIn"
        }),
        ...mapMutations({
                setLogin: "setLogin",
                setPasword: "setPassword"
            }),

        async signIn(){
            if (this.isFormValid){
                this.setLogin(this.login);
                this.setPasword(this.passwordHash);
                await this.SignInAction()
                this.$emit('exit');
            }
        }
    }
}
</script>
