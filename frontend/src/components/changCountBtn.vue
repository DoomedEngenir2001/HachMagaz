<template>
    <div class="chnge-count-btn">
        <div @click="minus" class="chg-btn">-</div>
        <div><slot></slot></div>
        <div @click="add" class="chg-btn">+</div>
    </div>
</template>
<script>
export default{
    methods:{
        add(){
            this.$emit('add');
        },
        minus(){
            this.$emit('minus');
        }
    }
}
</script>
<style>
.chnge-count-btn{
    display: flex;
    flex-direction: row;
    width: 90px;
    height: 25px;
    font-size: 20px;
    color: #5C6370;
    justify-content: center;
    align-items: center;
    background-color: #fffae2;
    border-radius: 25px;
}
.chg-btn{
    width: 16px;
    height: 16px;
    border-radius: 10px;
    font-size: 20px;
    text-align: center;
    line-height: 16px;
    background-color: #fffae2;
    color: #5C6370;
}
.chg-btn:hover{
    color:white;
    background-color:#5C6370;
}
</style>