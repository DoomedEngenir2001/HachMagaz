<template>
    <button class="nav-btn"><slot></slot></button>
</template>
<script>
export default{

}
</script>
<style scoped>
.nav-btn{
    min-width: 123px;
    width: wrap;
    height: 50px;
    background-color:#ffffff;
    color: #000000;
    font-size: 20px;
    border-radius: 20px;
}
.nav-btn:hover{
    background-color:#000000;
    color: #ffffff;
}
</style>