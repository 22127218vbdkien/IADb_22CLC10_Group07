<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';
import router from '@/router';
import axios from 'axios';
import AnimeSearchAndFilter from '@/components/search_filter/AnimeSearchAndFilter.vue';

const animes = reactive({
    state: {}
})

const searchAnime = async () => {
    try{
        const response = await  axios.get('/api/animes/',{
            params:{ 
                anime_format: "",
                status:"",
                source:""
            }
        })
        animes.state = response.data
        console.log(animes.state)
    } catch (error) {
        console.log(error)
    }
} 

</script>

<template>
    <AnimeSearchAndFilter></AnimeSearchAndFilter>
</template>