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
    height: 100px;
    background-color:#ffffff;
    margin-left: 10%;
    margin-right: 10%;
    border: none;
    color: #000000;
    font-size: 20px;
}
.nav-btn:hover{
    background-color:#000000;
    color: #ffffff;
}
</style>