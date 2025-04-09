<template>
    <button class="btn"><slot></slot></button>
</template>
<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: "orangeBtnTS"
});
</script>
<style scoped>
.btn{
    min-width: 144px;
    width: wrap;
    height: 50px;
    background-color:#ff6900;
    color: white;
    font-size: 20px;
    border-radius: 20px;
    border: none;
}
.btn:hover{
    background-color:#FFF0E6;
    color: #DB7A35;
}
</style>