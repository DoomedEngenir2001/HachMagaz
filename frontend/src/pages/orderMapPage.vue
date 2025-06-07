<template>
    <div>
    <yandex-map
        v-model="map"
        :settings="{
          location: {
            center: [128.858795, 71.629263 ],
            zoom: 15,
          },
        }"
        width="100%"
        height="1800px"
       >
      <yandex-map-default-scheme-layer/>
      <yandex-map-default-features-layer/>
      <yandex-map-default-marker v-if="selectedSearch" :settings="{  coordinates: selectedSearch }"/>
      </yandex-map>
      <div class="h-wrap p-[5px] bg-white fixed bottom-[50px] left-[30px] rounded-2xl">
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
  import { ElNotification } from 'element-plus';
    const selectedSearch = ref<LngLat | null>(null);
    const address = ref('');
    const padik = ref('');
    const doorCode = ref('');
    const stage = ref('');
    const flat = ref('')
    const comment = ref('')
    var dist = 0.0;
    const center = [128.858795, 71.629263 ]
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
            dist = Math.sqrt(Math.pow(selectedSearch.value[0]-center[0], 2)+
          Math.pow(selectedSearch.value[1]-center[1], 2)) *111.1;
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
      if (adressValid && dist <50) {
        let fullAddr = address.value + " подъезд " + padik.value + " Этаж " + stage.value + " Квартира " + flat.value;
        let info = "Код от двери "  + doorCode.value + " Комментарий " + comment.value;
        store.commit('setAddress', fullAddr);
        router.push('/order');
      } else if (adressValid && dist > 50){
        router.push("/");
          return ElNotification({
              title: 'Ошибка',
              message: 'Невозможно сюда доставить заказ',
              type: 'error',
              duration: 5000,
              position: 'bottom-right',
          });
      }
    };
  //Можно использовать для различных преобразований
  const map = shallowRef<null | YMap>(null);
  </script>