<template>
    <div class="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center ">
        <div class="flex-column items-center w-wrap h-wrap bg-white rounded-3xl p-[8px] ">
            <div class="flex-row w-full h-2/10">
                <cancelBtn @click="this.$emit('closeFormSignUp');" class="m-r-0 m-l-auto"></cancelBtn>
            </div>
            <div class="h-[105px] w-full text-4xl leading-[105px] text-center font-bold md:test-xl">Регистрация</div>
            <div class="h-[30px] w-full mt-[5px] text-xl leading-[30px] font-bold">Логин</div>
            <input v-model="this.login" placeholder="Введите логин" class="outline lg:w-[630px] lg:h-[75px] mt-[5px] rounded-3xl 
            md:w-[310px] md:h-[50px]">
            <span v-if="this.submitted && !this.loginIsValid" class="flex text-base text-red-600">Это поле должно быть заполнено!</span>
            <div class="h-[30px] w-full mt-[5px] text-xl leading-[30px] font-bold">Пароль</div>
            <input v-model="this.password" type="password" placeholder="Введите пароль" class="outline lg:w-[630px] lg:h-[75px] mt-[5px] rounded-3xl
            md:w-[310px] md:h-[50px]">
            <span v-if="this.submitted && !this.passwordIsValid"class="flex text-base text-red-600">Пароль должен состоять, как минимум из пяти символов!</span>
            <div class="h-[30px] w-full mt-[5px] text-xl leading-[30px] font-bold">Email</div>
            <input v-model="this.email" placeholder="Введите почту" class="outline lg:w-[630px] lg:h-[75px] mt-[5px] rounded-3xl
            md:w-[310px] md:h-[50px]">
            <span v-if="this.submitted && !this.emailIsValid" class="flex text-base text-red-600">Это поле должно быть заполнено!</span>
            <div class="h-[30px] w-full mt-[5px] text-xl leading-[30px] font-bold">Телефон</div>
            <input v-model="this.phone" placeholder="Введите номер телефона" class="outline lg:w-[630px] lg:h-[75px] mt-[5px] rounded-3xl
            md:w-[310px] md:h-[50px]">
            <span v-if="this.submitted && !this.phoneIsValid" class="flex text-base text-red-600">Это поле должно быть заполнено!</span>
            <div class="mt-[10px] flex text-center text-gray text-2xl justify-center"> <orangeBtn class="w-[220px]" @click="this.$emit('toSignIn');">Войти</orangeBtn></div>
            <div class="mt-[20px] flex w-full text-center justify-center"><orangeBtn  @click="signUp()" class="text-white w-[220px] ">Зарегистрироваться</orangeBtn></div>    
        </div>
    </div>
    </template>
    <script>

    import { mapActions, mapMutations } from "vuex";
    import cancelBtn from "./cancelBtn.vue";
    import orangeBtn from "./orangeBtn.vue";
    import sha256 from 'js-sha256';
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
                phone: "",
                submitted: false
            }
        },
        computed:{
            loginIsValid(){
                if (this.login !=="") return true;
                else return false;
            },
            passwordIsValid(){
                if (this.password.length > 4) return true;
                else return false;
            },
            emailIsValid(){
                const template = /@/
                return template.test(this.email);
            },
            phoneIsValid(){
                const template = /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/
                return template.test(this.phone);
            },
            isFormValid(){
                this.submitted = true;
                return this.loginIsValid && this.passwordIsValid && this.emailIsValid && this.phoneIsValid
            },
            passwordHash(){
                return sha256(this.password);
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
                if(this.isFormValid){
                    this.setEmail(this.email);
                    this.setPhone(this.phone);
                    this.setLogin(this.login);
                    this.setPasword(this.passwordHash);
                    await this.SignUp();
                    this.$emit('toSignIn');
                }

            }
        }
    }
    </script>
    