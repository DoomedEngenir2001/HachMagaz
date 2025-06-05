<template>
    <div class="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center ">
        <div class="flex-column items-center w-wrap h-wrap bg-white rounded-3xl 
        p-[8px] w-[400px] h-[200px]">
            <div class="flex-row w-full h-1/10">
                <cancelBtn @click="this.$emit('closeContact');" class="m-r-0 m-l-auto"></cancelBtn>
            </div>
            <div class="flex flex-col text-xl">
                <div class="text-center font-bold">Контакная информация</div>
                <div class="flex flex-row mt-[10px] "><div class="font-bold">Адрес:</div><div class="ml-[10px]">пгт. Тикси, Ленинская улица, 25</div></div>
                <div class="flex flex-row mt-[10px] "><div class="font-bold">Владелец:</div><div class="ml-[10px]">Ибрагимов Ашот Вазгенович</div></div>
                <div class="flex flex-row mt-[10px] "><div class="font-bold">Телефон:</div><div class="ml-[10px]">89997776655</div></div>
            </div>
        </div>
    </div>
</template>
    <script>
    import cancelBtn from "./cancelBtn.vue";
    export default {
        name: "contactModal",
        components: {
            cancelBtn,
        },
    }
    </script>