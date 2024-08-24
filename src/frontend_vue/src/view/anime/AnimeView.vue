<script setup>
    import router from '@/router';
    import { RouterLink,  useRoute, useRouter} from 'vue-router';
    import { onMounted, reactive } from 'vue';
    import axios from 'axios';
    const _route = useRoute()
    const _router = useRouter()
    const _animeid = _route.params.id
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
            const response = await axios.get(`/api/animes/${_animeid}/`)
            animeState.property = response.data
            console.log( animeState.property )
        } catch (error) {
            console.log(error)
        }
    })
</script>

<template>
    <div class="banner-image">
        <img :src="`${animeState.property.banner_img}`" alt="">
    </div>
    <div class="container">
        <div class="container" id="image_and_button">
            <div class="cover-image-lagre">
                <img :src="`${animeState.property.cover_img_large}`" alt="">
            </div>
            <div class="px-4 py-2 bg-blue-200 text-blue-800 border-blue-800 hover:bg-blue-400 max-w-max rounded-xl border-2">Add to list</div>
        </div>

        <div class="container" id="tag_and_description">
            <div>
                <p>{{ animeState.property.romaji_title}}</p>
            </div>
        </div>
    </div>
    
    
</template>