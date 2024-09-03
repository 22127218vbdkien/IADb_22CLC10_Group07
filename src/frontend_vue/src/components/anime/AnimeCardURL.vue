<script setup>
    import { defineProps, reactive, onMounted } from 'vue';
    import { RouterLink } from 'vue-router';
    import axios from 'axios';
    const props = defineProps({
        url: String,
    })
    const animeState = reactive({
        property:{
            id: 0,
            id_anilist: 0,
            id_mal: 0,
            romaji_title: "",
            english_title: "",
            native_title: "",
            format: "",
            status: "",
            description: "",
            start_date: "",
            end_date: "",
            episodes: 0,
            duration: 0,
            source: "",
            hashtag: "",
            trailer: "",
            cover_img_large: "",
            cover_img_med: "",
            banner_img: "",
            anilist_score: 0, 
            mean_score: 0,
            popularity: 0,
            trending:0,
            favorites:0, 
            tags: [],
            relations: [], 
            characters: [],
            staffs: [],
            studios: [],
            links: [],
        }})
    
    onMounted(async ()=>{
        try {
            const response = await axios.get(props.url)
            animeState.property = response.data
        } catch (error) {
            console.log(error)
        }
    })
</script>

<template>
    <div class="card-container hover:border-blue-600 hover:border-4 hover:border-dashed w-40 px-1 py-2">
        <RouterLink :to="`/animes/${animeState.property.id}/`">
            <div>
            <img :src="animeState.property.cover_img_large" alt="Anime Image"/>
            <div class="text-sm mt-1">{{ animeState.romaji_title }}</div>
            </div>
        </RouterLink>
        
    </div>
    
</template>