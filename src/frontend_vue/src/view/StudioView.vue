<script setup>
import { initCustomFormatter, onMounted, reactive } from 'vue';
import axios from 'axios';
import AnimeCard from '@/components/anime/AnimeCard.vue';
import { info } from 'autoprefixer';
import { useRoute, useRouter } from 'vue-router';
import { extractRuntimeProps } from 'vue/compiler-sfc';
const _route = useRoute()
const _router = useRouter()
const studio_id = _route.params.id
const studio = reactive({
    info: {
        url: null,
        id: null,
        name: null,
        favorites: 0,
        animes:[],
    }
})


onMounted(async () => {
    try{
        const response = await axios.get(`/api/studios/${studio_id}/`)
        if (response.status === 200){
            studio.info = response.data
        }
    }catch(error){
        console.log(error)
    }
})
</script>

<template>
    
    <section class="max-w-6xl mx-auto mt-10 mb-4 px-4 py-2">
        <div class="mb-4">
            <h1 class="text-gray-700 font-bold text-2xl">
                Studio Name
            </h1>
            <div class="text-gray-700 font-medium text-xl"> {{ studio.info.name }}</div>
        </div>
        <div class="max-w-full flex items-center justify-between flex-col">
            <h1 class="text-gray-700 font-bold text-2xl mb-2">
                Produced by {{ studio.info.name }}
            </h1>
            <div id="anime-frame-frame" class="grid grid-cols-5 max-w-5xl gap-x-10 gap-y-4 grid-flow-row">
                <AnimeCard v-for="anime in studio.info.animes" :key="anime.id" :anime="anime"></AnimeCard>
            </div>
        </div>
    </section>
</template>