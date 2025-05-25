<template>
    <div class="flex items-center">
        <div class="flex gap-3 items-center">
            <slot name="pre-append">
            </slot>
            <input class="border-solid border border-gray rounded-sm pl-1 h-8 min-w-xl"
            v-model="query"/>
        </div>
        <slot name="append">
        </slot>
    </div>
</template>
<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({

    emits: ['changeProducts'],
    setup(props, {emit} ) {
//  TODO пошук очень нобычно работает (попробуй пицца, потом удалить и написать энергетик и проскролить ленту ))))
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