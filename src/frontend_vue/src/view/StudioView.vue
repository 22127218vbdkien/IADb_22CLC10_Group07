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
    <section id="studio-info">
        <h1>Studio Name</h1>
        <div> {{ studio.info.name }}</div>
    </section>
    <section>
        <h2>Anime produced by studio</h2>
        <div id="anime-frame">
            <AnimeCard v-for="anime in studio.info.animes" :key="anime.id" :anime="anime"></AnimeCard>
        </div>
    </section>
</template>