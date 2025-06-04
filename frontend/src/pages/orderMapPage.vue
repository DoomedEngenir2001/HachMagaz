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
      <div class="h-wrap p-[5px] bg-white fixed bottom-[10px] left-[10px] rounded-2xl">
        <div class="flex flex-col w-[250px] md:w-[320px] h-wrap">
            <div class="w-full font-bold lg:h-[20px] text-lg text-center mt:h-[15px]">Укажите ваш адрес</div>
            <input v-model="address" list="search" placeholder="Город, улица и дом" class="flex w-full 
            lg:h-[45px] rounded-2xl border mt-[14px]"/>
            <datalist id="search" class="flex-column">
            <option 
                  v-for="(item, index) in searchResponse ?? []"
                  :key="item.geometry?.coordinates.join(',') ?? index"
                  :value="item.properties.name+' ('+ item.properties.description+')'"
                  hidden>
            </option>
            </datalist>
            <span v-if=" !adressValid" 
            class="flex text-base text-red-600">Укажите адрес!</span>
            <div class="flex-row flex w-full lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]">
              <input v-model="padik" placeholder="Подъезд" class="flex-row flex w-1/2 
                lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]"/>
                <input v-model="doorCode" placeholder="Код от двери" class="flex-row flex w-1/2
                lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]"/>
            </div>
            <div class="flex-row flex w-full lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]">
              <input v-model="stage" placeholder="Этаж" class="flex-row flex w-1/2 
              lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]"/>
              <input v-model="flat" placeholder="Квартира" class="flex-row flex w-1/2 
              lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]"/>
            </div>
            <input  v-model="comment" placeholder="Комментарий" class="flex-row flex w-full
              lg:h-[31px] md:h-[20px] lg:mt-[14px] md:mt-[7px]"/>
            <orangeBtnTS @click="SubmitOrder" class="mt-[14px] 
            w-full h-[50px]">Заказать отсюда</orangeBtnTS>
        </div>
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
    var adressValid = false; 
    var submitted = false;
    function sleep(ms: number) {
        return new Promise(resolve => setTimeout(resolve, ms));
      }

    watch(address, async val => {
      if (!val) return;
      else{
        searchResponse.value = await ymaps3.search({
            text: val,
            bounds: map.value?.bounds,
          });
        searchResponse.value.forEach(el => {
          if (address.value === el.properties.name +' ('+ el.properties.description+')'){
            selectedSearch.value = el.geometry?.coordinates as LngLat;
            return;
          }
      })
      adressValid = true;
      }
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
      submitted = true;
      if (adressValid) {
        let fullAddr = address.value + " подъезд " + padik.value + " Этаж " + stage.value + " Квартира " + flat.value;
        let info = "Код от двери "  + doorCode.value + " Комментарий " + comment.value;
        store.commit('setAddress', fullAddr);
        router.push('/order');
      }
    };
  //Можно использовать для различных преобразований
  const map = shallowRef<null | YMap>(null);
  </script>