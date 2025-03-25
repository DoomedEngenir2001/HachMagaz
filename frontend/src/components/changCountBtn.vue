<template>
    <div class="chnge-count-btn">
        <div class="chg-btn">-</div>
        <div><slot></slot></div>
        <div>+</div>
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
    width: 60px;
    height: 25px;
    font-size: 20px;
    color: #5C6370;
    justify-content: center;
    align-items: center;
}
.chg-btn{
    width: 16px;
    height: 16px;
    border-radius: 10px;
    background-color: white;
    color: #5C6370;
}
.chg-btn:hover{
    color:white;
    background-color:#5C6370;
}
</style>