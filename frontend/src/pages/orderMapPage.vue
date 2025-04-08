<template>
    <div>
    <yandex-map
        v-model="map"
        :settings="{
          location: {
            center: [30.31, 59.93 ],
            zoom: 9,
          },
        }"
        width="100%"
        height="1800px"
       >
      <yandex-map-default-scheme-layer/>
      <yandex-map-default-features-layer/>
      <yandex-map-default-marker v-if="selectedSearch" :settings="{  coordinates: selectedSearch }"/>
      </yandex-map>
      <div class="w-[320px] h-wrap p-[10px] bg-white flex-column 
        fixed bottom-[79px] left-[70px] rounded-2xl">
        <div class="w-100% h-[65px] text-lg">Передвиньте маркер
            или укажите ваш адрес</div>
          <input v-model="address" list="search" placeholder="Город, улица и дом" class="w-[300px] h-[45px] rounded-2xl border mt-[14px]"/>
              <datalist id="search" class="flex-column">
                  <option 
                      v-for="(item, index) in searchResponse ?? []"
                      :key="item.geometry?.coordinates.join(',') ?? index"
                      :value="item.geometry?.coordinates"
                      >
                      {{ item.properties.name }} ({{ item.properties.description }})
                  </option>
                </datalist>
        <div class="flex-row w-[300px] h-[31px] mt-[14px]">
            <input v-model="padik" placeholder="Подъезд" class="w-[145px] h-[31px] rounded-2xl border"/>
            <input v-model="doorCode" placeholder="Код от двери" class="w-[145px] h-[31px] rounded-2xl border ml-[10px]"/>
        </div>
        <div class="flex-row w-[300px] h-[31px] mt-[14px]">
            <input v-model="stage" placeholder="Этаж" class="w-[145px] h-[31px] rounded-2xl border"/>
            <input v-model="flat" placeholder="Квартира" class="w-[145px] h-[31px] rounded-2xl border ml-[10px]"/>
        </div>
        <input  v-model="comment" placeholder="Комментарий" class="w-[300px] h-[45px] rounded-2xl border mt-[14px]"/>
        <orangeBtnTS @click="SubmitOrder" class="mt-[14px] w-[306px] h-[50px]">Заказать отсюда</orangeBtnTS>
    </div>
    </div>    
  </template>
  
  <script setup lang="ts">
  import { ref, shallowRef, watch } from 'vue';
  import type { LngLat, YMap } from '@yandex/ymaps3-types';
  import { YandexMap, YandexMapDefaultSchemeLayer, YandexMapDefaultFeaturesLayer,
    YandexMapDefaultMarker, } from 'vue-yandex-maps';
  import type { SearchResponse } from '@yandex/ymaps3-types/imperative/search';
  import orangeBtnTS from "../components/orangeBtnTS.vue";
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
    const selectedSearch = ref<LngLat | null>(null);
    const address = ref('');
    const padik = ref('');
    const doorCode = ref('');
    const stage = ref('');
    const flat = ref('')
    const comment = ref('')
    const searchResponse = shallowRef<null | SearchResponse>(null);
    const store = useStore();
    const router = useRouter();
    function sleep(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

    watch(address, async val => {
        if (!val) return;

    // Проверка, что уже координаты
    if (val.split(/[,.]/).length === 4) {
        let copy = val;
        selectedSearch.value = copy.split(',').map(x => parseFloat(x)) as LngLat;
        return;
    }
    await sleep(300);
    if (val !== address.value) return;
    searchResponse.value = await ymaps3.search({
        text: val,
        bounds: map.value?.bounds,
      });
    });

    watch([selectedSearch], async () => {
        if ( selectedSearch.value) {
          
        map.value?.setLocation({
            center: selectedSearch.value,
            zoom: 15,
            duration: 300,
        });
      }
    });

    const SubmitOrder = () => {
        let fullAddr = address.value + " подъезд " + padik.value + " Этаж " + stage.value + " Квартира " + flat.value;
        let info = "Код от двери "  + doorCode.value + " Комментарий " + comment.value;
        store.commit('setAddress', fullAddr);
        router.push('/order');
    };
  //Можно использовать для различных преобразований
  const map = shallowRef<null | YMap>(null);
  </script>