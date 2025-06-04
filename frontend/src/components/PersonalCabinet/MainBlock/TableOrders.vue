<script lang="ts">
import type { DataTableColumns } from 'naive-ui'
import { defineComponent } from 'vue'
import { useStore } from 'vuex'

interface RowData {
    name: string
    date_transaction: string
    adres: string
    children?: ProductCard[]
}

interface ProductCard {
    product: string,
    price: number,
    description: string,
    imagePath: string,
    id: number
}
// Test git
export default defineComponent({
    setup() {
        const store = useStore();
        const data: RowData[] = store.getters.getOrders;
        // [
        //     {
            //     name: 'Заказ №666',
            //     date_transaction: '16.05.2025 12.34',
            //     adres: 'г. Лохушкана, дом колотушкина',
            //     children: [
            //         {
            //             product: 'Сосиска в попе',
            //             price: 100500,
            //             description: 'Очень вкусно, но пахнет фекалиями',
            //             id: 100,
            //             imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
            //         },
            //         {
            //             product: 'Сосиска в попе',
            //             price: 100500,
            //             description: 'Очень вкусно, но пахнет фекалиями',
            //             id: 100,
            //             imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
            //         },
            //         {
            //             product: 'Сосиска в попе',
            //             price: 100500,
            //             description: 'Очень вкусно, но пахнет фекалиями',
            //             id: 100,
            //             imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
            //         },
            //         {
            //             product: 'Сосиска в попе',
            //             price: 100500,
            //             description: 'Очень вкусно, но пахнет фекалиями',
            //             id: 100,
            //             imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
            //         }
            //     ]
            // },
            // {
            //     name: 'Заказ №667',
            //     date_transaction: '18.05.2025 14.34',
            //     adres: 'г. Лохушкана, дом колотушкина',
            //     children: [
            //         {
            //             product: 'Сосиска в попе',
            //             price: 100500,
            //             description: 'Очень вкусно, но пахнет фекалиями',
            //             id: 100,
            //             imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
            //         }
            //     ]
            // },
        // ]

        const columns: DataTableColumns<RowData> = [
            {
                title: '№ заказа',
                width: 50,
                titleAlign: 'center',
                key: 'id'
            },
            {
                title: 'Время заказа',
                width: 30,
                align: 'center',
                key: 'createTime'
            },
            // {
            //     title: 'Хавчик',
            //     width: 70,
            //     align: 'center',
            //     key: 'product'
            // },
            // {
            //     title: 'Стоимость',
            //     width: 70,
            //     align: 'center',
            //     key: 'price'
            // },
            // {
            //     title: 'Описание',
            //     titleAlign: 'center',
            //     align: 'center',
            //     width: 70,
            //     key: 'description'
            // },
            {
                title: 'Адрес доставки',
                width: 70,
                align: 'center',
                key: 'address'
            },
        ]

        const rowKey = (row: RowData) => row.name

        return { columns, data, rowKey }
    }
})
</script>
<template>
    <n-data-table :columns="columns" :data="data" :tree="true" :bordered="true" :row-key="rowKey" />
</template>
