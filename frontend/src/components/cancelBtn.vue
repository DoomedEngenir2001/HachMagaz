<template>
    <div class="cancelButton"></div>
</template>
<script>
export default{

}
</script>
<style>
.cancelButton{
    width: 35px;
    height:35px;
    background-image: url(~@/assets/close.png);
    background-size:contain;
    margin-left: auto;
    margin-right: 0;
}
.cancelButton:hover{
    background-image: url(~@/assets/close_inv.png);
}
</style>