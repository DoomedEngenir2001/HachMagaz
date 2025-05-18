<script lang="ts">
import type { DataTableColumns } from 'naive-ui'
import { defineComponent } from 'vue'

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
        const data: RowData[] = [
            {
                name: 'Заказ №666',
                date_transaction: '16.05.2025 12.34',
                adres: 'г. Лохушкана, дом колотушкина',
                children: [
                    {
                        product: 'Сосиска в попе',
                        price: 100500,
                        description: 'Очень вкусно, но пахнет фекалиями',
                        id: 100,
                        imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
                    },
                    {
                        product: 'Сосиска в попе',
                        price: 100500,
                        description: 'Очень вкусно, но пахнет фекалиями',
                        id: 100,
                        imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
                    },
                    {
                        product: 'Сосиска в попе',
                        price: 100500,
                        description: 'Очень вкусно, но пахнет фекалиями',
                        id: 100,
                        imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
                    },
                    {
                        product: 'Сосиска в попе',
                        price: 100500,
                        description: 'Очень вкусно, но пахнет фекалиями',
                        id: 100,
                        imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
                    }
                ]
            },
            {
                name: 'Заказ №667',
                date_transaction: '18.05.2025 14.34',
                adres: 'г. Лохушкана, дом колотушкина',
                children: [
                    {
                        product: 'Сосиска в попе',
                        price: 100500,
                        description: 'Очень вкусно, но пахнет фекалиями',
                        id: 100,
                        imagePath: 'https://www.naiveui.com/assets/naivelogo-BdDVTUmz.svg'
                    }
                ]
            },
        ]

        const columns: DataTableColumns<RowData> = [
            {
                title: '№ заказа',
                width: 50,
                titleAlign: 'center',
                key: 'name'
            },
            {
                title: 'Время заказа',
                width: 30,
                align: 'center',
                key: 'date_transaction'
            },
            {
                title: 'Хавчик',
                width: 70,
                align: 'center',
                key: 'product'
            },
            {
                title: 'Стоимость',
                width: 70,
                align: 'center',
                key: 'price'
            },
            {
                title: 'Описание',
                titleAlign: 'center',
                align: 'center',
                width: 70,
                key: 'description'
            },
            {
                title: 'Адрес доставки',
                width: 70,
                align: 'center',
                key: 'adres'
            },
        ]

        const rowKey = (row: RowData) => row.name

        return { columns, data, rowKey }
    }
})
</script>
<template>
    <div class="flex w-full center pl-5 pr-5 h-full pb-1w0">
        <n-data-table :columns="columns" :data="data" :tree="true" :bordered="true" :row-key="rowKey" />
    </div>
</template>
