<template>
  <el-dialog
    :model-value="props.hideModal"
    title="Добавить карточку товара"
    @closed="closeModal"
  >
    <el-form :model="form">
      <el-form-item label="Promotion name">
        <el-input v-model="form.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="Zones">
        <el-select v-model="form.region" placeholder="Please select a zone">
          <el-option label="Zone No.1" value="shanghai" />
          <el-option label="Zone No.2" value="beijing" />
        </el-select>
      </el-form-item>
    </el-form>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeModal">Cancel</el-button>
        <el-button type="primary" @click="closeModal"> Confirm </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { reactive, ref } from "vue";

export default defineComponent({
  props: {
    hideModal: {
      type: Boolean,
      default: true,
      required: true,
    },
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
      console.log("closeModal");
      emit("closeModalAction");
    };
    return { form, closeModal, props };
  },
});
</script>
