<template>
  <div class="w-full flex flex-col justify-center">
    <HeaderPageAdmin />
    <div class="w-95/100 h-95/100 flex flex-col items-center">
      <EditCardDialog
        :hideModal="isOpenModal"
        :v-model="isOpenModal"
        :dataCard="currentCard"
        @close-modal-action="closeModal"
      />
      <searchCardItem class="w-9/10 flex justify-between mt-5 mb-5 h-fit">
        <template #pre-append>
          <el-icon :size="30"><Search /></el-icon>
        </template>
        <template #append>
          <el-icon @click="openModal" :size="30" class="hover:scale-150"
            ><DocumentAdd
          /></el-icon>
        </template>
      </searchCardItem>

      <div
        class="w-9/10 flex flex-col border-solid border border-gray bg-slate-300 rounded-xl items-center"
      >
        <productCardEdit
          @editCard="onEdit(item)"
          v-for="item in store.getters.getQueryProducts"
          :key="item.id"
          :name="item.product"
          :price="item.price"
          :description="item.description"
          :image="item.image"
          :id="item.id"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, Ref } from "vue";
import { ref } from "vue";
import { useStore } from "vuex";
import { DocumentAdd, Search } from "@element-plus/icons-vue";
import OrangeBtnTS from "../components/orangeBtnTS.vue";
import productCardEdit from "../components/productCardEdit.vue";
import searchCardItem from "../components/searchCardItem.vue";
import HeaderPageAdmin from "../components/HeaderPageAdmin.vue";
import EditCardDialog from "../components/editCardDialog.vue";
import type CardInterface from '../share/interfaces/card.ts'


export default defineComponent({
  setup() {
    const store = useStore();
    store.dispatch("getAllProductCards");
    const isOpenModal = ref(false);
    let currentCard: Ref<CardInterface>= ref(
      {
      count:0,
      description:'',
      imagePath: '',
      name: '',
      price:0,
      id: 0
    })

    function onEdit (card:CardInterface){
      isOpenModal.value = true;
      currentCard.value = card
    };
    const openModal = () => {
      isOpenModal.value = true;
      console.log("openModal: isOpenModal.value", isOpenModal.value)
    };
    const closeModal = () => {
      isOpenModal.value = false;
      currentCard.value = {
        count: 0,
        description:'',
        id:0,
        imagePath:'',
        name:'',
        price:0,
      }
      console.log("closeModal", isOpenModal.value);
    };
    return { isOpenModal, onEdit, openModal, closeModal, store, currentCard };
  },
  components: {
    DocumentAdd,
    Search,
    OrangeBtnTS,
    productCardEdit,
    searchCardItem,
    HeaderPageAdmin,
    EditCardDialog,
  },
});
// http://localhost:5173/adminPage
// адрес странички
</script>
<style>
.plus {
  background-image: url(../assets/plus.png);
}
</style>
