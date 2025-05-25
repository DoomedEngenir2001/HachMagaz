<template>
  <el-dialog
    :model-value="props.hideModal"
    title="Добавить карточку товара"
    width="80%"
    @closed="closeModal"
  >
    <div class="flex flex-row justify-between ">
      <el-card>
        <template #header>
             Превью для Юзера
        </template>
             {{ dataCard }}
        </el-card
      >
      <el-card>
        <template #header>
             Тут ты меняешь
        </template>
             {{ dataCard }}
        </el-card
      >
    </div>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeModal">Cancel</el-button>
        <el-button type="primary" @click="closeModal"> Confirm </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts">
import { reactive, ref, defineComponent } from "vue";
import type CardInterface from '../share/interfaces/card.ts'

export default defineComponent({
  props: {
    hideModal: {
      type: Boolean,
      default: true,
      required: true,
    },
    dataCard: {
      description: '',
      imagePath: '',
      name: '',
      count: 0,
      price: 0,
      id: 0
    } as CardInterface,
  },
  emits: ["closeModalAction"],
  setup(props, { emit }) {
    let form = reactive({
      name: "",
      region: "",
      date1: "",
      delivery: false,
      type: [],
      resource: "",
      desc: "",
    });
    const closeModal = () => {
      emit("closeModalAction")
    };
    return { form, closeModal, props };
  },
});
</script>
