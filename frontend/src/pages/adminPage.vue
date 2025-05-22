<template>
<div class="w-full flex flex-col justify-center">
    <HeaderPageAdmin/>
    <div class="w=95/100 h-95/100 flex flex-col items-center">
        <searchCardItem class=" flex mt-[10px] mb-[10px] "/>
        <div class="w-9/10 flex flex-col border-solid border border-gray bg-slate-300 rounded-xl
        items-center">
            <productCardEdit @editCard="onEdit()" v-for="item in productCards"
            :name="item.product" :price="item.price" :description="item.description"
            :image="item.image" :id="item.id"/>
        </div>
        <OrangeBtnTS @editCard="onEdit()" class="w-5/10 mt-[5px]">Добавить</OrangeBtnTS>
        <editCardDialog v-if="hideModal == false"/>
    </div>
</div>
</template>
<script lang="ts">
import { useStore } from 'vuex';
import OrangeBtnTS from '../components/orangeBtnTS.vue';
import productCardEdit from '../components/productCardEdit.vue';
import searchCardItem from '../components/searchCardItem.vue';
import HeaderPageAdmin from '../components/HeaderPageAdmin.vue';
import editCardDialog from '../components/editCardDialog.vue';
import { defineComponent } from 'vue';
import { ref } from 'vue';
export default defineComponent({
    setup(){
        const store = useStore();
        store.dispatch("getAllProductCards");
        const productCards = store.getters.getProductsfromState;
        const hideModal = ref(true);
        const onEdit = () => {
            hideModal.value = false;
        }
        return {productCards, hideModal, onEdit}
    },
    components:{
        OrangeBtnTS, productCardEdit, searchCardItem, HeaderPageAdmin, editCardDialog
    }
})
// http://localhost:5173/adminPage
// адрес странички
</script>