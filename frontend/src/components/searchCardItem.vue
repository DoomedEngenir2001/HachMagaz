<template>
    <input class="border-solid border border-gray  rounded-xl 
    w-9/10 h-[50px] flex justify-center"
    v-model="query"/>
</template>
<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
    emits: ['changeProducts'],
    setup(props, {emit} ) {
        const store = useStore();
        const query = ref('');
        watch(query, val => {
            if(val){
                store.dispatch("getProductCardOnInput", val);
            }else {
                store.commit("setQueryProducts", store.getters.getProductsfromState);
            }
        });
        return {query}
    },
})
</script>