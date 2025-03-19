<template>
    <button class="btn"><slot></slot></button>
</template>
<script>
export default{

}
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
}
.btn:hover{
    background-color:#FFF0E6;
    color: #DB7A35;
}
</style>