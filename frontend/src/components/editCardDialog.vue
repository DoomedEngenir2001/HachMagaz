<template>
  <el-dialog
    :model-value="props.hideModal"
    title="Добавить карточку товара"
    width="80%"
    @closed="closeModal">
    <div class="flex flex-row justify-between ">
      <el-card>
        <template #header>
             <div class="product-card">
                <div class="image-placeholder">
                    <img :src="dataCard.imagePath" alt="image" class="product-image" @click="showModal">
                </div>
                <div class="product-name">{{dataCard.product}}</div>
                <div class="price-holder">
                    <div>{{dataCard.price}} рублей</div>
                </div>
            </div>
        </template>
      </el-card>
      <el-card>
        <template #header>
             <div class="product-card">
               <el-upload
                  class="upload-demo"
                   drag
                   multiple
                 />
                <el-input class="product-name" v-model="dataCard.product"></el-input>
                <div class="price-holder">
                    <el-input v-model="dataCard.price">рублей</el-input>
                </div>
            </div>
        </template>
        </el-card>
    </div>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeModal" type="warning">отменить</el-button>
        <el-button type="primary" @click="closeModal">Добавить</el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts">
import { reactive, ref, defineComponent } from "vue";
import type CardInterface from '../share/interfaces/card.ts'
import ProductCard from "./productCard.vue";
import { UploadFilled } from '@element-plus/icons-vue'

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

<style>
.product-card{
    width: 450px;
    height: 500px;
    /* margin-right: 42.5px; */
    display: flex;
    flex-direction: column;
    border: 5px solid rgba( 128,128,128, 0.4);
    border-radius: 10px;
    /* box-shadow:  5px 5px rgb(175, 175, 175); */
}
.image-placeholder{
    width: 100%;
    height: 357px;
    display: flex;
    background-image: url("../assets/phone.png");
}
.product-image{
    width: 100%;
    height: 355px;
    display: flex;
    object-fit: contain;
}
.product-name{
    height: wrap;
    padding-left: 5px ;
    font-size: 32px;
    font-weight: bold;
}
.price-holder{
    height: wrap;
    display: flex;
    flex-direction: row;
    padding-left: 5px ;
    padding-right: 5px;
    font-size: 40px;
}
.toRightCorner{
    margin-left: auto; 
    margin-right: 0;
}
.el-upload-dragger{
  height: 380px;
}
</style>