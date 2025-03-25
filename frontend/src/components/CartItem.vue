<template>
<div class="cart-item">
    <div style="width: 100%;"><cancelBtn @click="this.deleteItem" class="toRight"></cancelBtn></div>
    <div class="central-content">
        <img :src="this.$props.imagePath" class="product-image"/>
        <p>{{this.$props.name}}</p>
    </div>
    <div class="footer">
        <p>{{ cost }} рублей</p>
        <changCountBtn class="toRight" @add="AddItem" @minus="MinusItem">{{this.$props.count}}
        </changCountBtn>
    </div>
</div>
</template>
<script>
import cancelBtn from './cancelBtn.vue';
import changCountBtn from './changCountBtn.vue';
import { mapMutations } from 'vuex';
export default{
    components:{
        cancelBtn,
        changCountBtn
    },
    props: {
        imagePath : {
            required: true,
            type: String
        },
        name:  {
            required: true,
            type: String
        },
        price: {
            required: true,
            type: Number
        },
        count: {
            required: true,
            type: Number
        },
    },
    computed: {
        cost(){
            return this.$props.count * this.$props.price;
        }
    },
    methods: {
        ...mapMutations({
            addCountByName : 'addCountByName',
            minusCountByName: 'minusCountByName',
            deleteItemByName: 'deleteItemByName'
        }),
        AddItem(){
            this.addCountByName(this.$props.name);
            console.log(this.$props.name+ " props")
        },
        MinusItem(){
            this.minusCountByName(this.$props.name);
        },
        deleteItem(){
            this.deleteItemByName(this.$props.name);
        }
    }
}
</script>
<style scoped>
.cart-item{
    margin-top: 5px;
    width: 100%;
    height: 230px;
    background-color: white;
    display: flex;
    flex-direction: column;
}
.central-content{
    display: flex;
    flex-direction: row;
    font-size: 24px;
    width: 100%;
    height: 140px;
    padding-left: 5px;
}
.product-image{
    width: 140px;
    height: 140px;
    background-size:contain;
}
.toRight{
    margin-right: 25px;
    margin-left: auto;
}
.footer{
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 20px;
    width: 100%;
    height: 60px;
}
</style>