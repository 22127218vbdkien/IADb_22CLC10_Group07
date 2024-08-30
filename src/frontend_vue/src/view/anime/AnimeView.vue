<script setup>
    import router from '@/router';
    import { RouterLink,  useRoute, useRouter} from 'vue-router';
    import {ref, onMounted, reactive, watch } from 'vue';
    import { userState } from '@/store/userStore';
    import axios from 'axios';
    import animeCollectionForm from '@/components/popup/animeCollectionForm.vue';
    import CharacterCard from '@/components/character/CharacterCard.vue';
    import StaffCard from '@/components/staff/StaffCard.vue';
    import AnimeCard from '@/components/anime/AnimeCard.vue';
    import AnimeCardURL from '@/components/anime/AnimeCardURL.vue';
    import Tag from '@/components/anime/Tag.vue';
    const _route = useRoute()
    const _router = useRouter()
    const _animeid = _route.params.id
    const showform = ref(false)
    const stateAuth = userState()
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
    watch(() => _route.params.id, async(newid) => {
        try {
            const response = await axios.get(`/api/animes/${newid}/`)
            animeState.property = response.data
            console.log( animeState.property )
        } catch (error) {
            console.log(error)
        }
    })
    const toggleCollectionForm = () =>{
        showform.value = !showform.value
    }
</script>

<template>
    
    <section class="with-banner">
        <div class="banner-image">
            <img :src="`${animeState.property.banner_img}`" alt="">
        </div>
        <div class="bg-blue-500 h-1 w-full mb-4">
        </div>
        <section id="anime-image-and-description" class="flex flex-row">
            <div class="container w-fit min-w-72 min-h-96 flex flex-col justify-center items-center">
                <div class="cover-image-lagre">
                        <img :src="`${animeState.property.cover_img_large}`" alt="">
                    </div>
                <div v-if="stateAuth.isAuthenticated" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
                    hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer" @click="toggleCollectionForm">Add to list</div>
            </div>
            
            <div id="anime-description flex flex-col justify-between items-center">
                <div class="text-2xl font-bold text-gray-500">
                    <h2>{{ animeState.property.romaji_title}}</h2>
                </div>
                <div id="description">{{ animeState.property.description || "This anime has no description" }}</div>
                
                <div id="tag-frame" v-if="animeState.property.tags" class="flex flex-row flex-wrap my-4">
                    <Tag v-for="item in animeState.property.tags" :key="item.id" :tag="item.tag" class="mx-0.5 my-0.5"></Tag>
                </div>
                <div class="flex flex-row ">
                    <div id="scores" class="text-green-600 mr-1"><i class="pi pi-star px-1"></i> {{ animeState.property.anilist_score || 'No info' }}</div>
                    <div id="favorites" class="text-red-600 mr-1"><i class="pi pi-heart px-1"></i>{{ animeState.property.favorites || 'No info' }}</div>
                </div>
            </div>
        
        </section>
    </section>
    
    <animeCollectionForm v-if="showform" :anime_id="Number(_animeid)" @modal-close="toggleCollectionForm"></animeCollectionForm>
    <div class="w-full flex flex-row justify-evenly items-center border-y-2 border-blue-500">
        <a class = "hover:text-blue-500" href="#details">Details</a>
        <a class = "hover:text-blue-500"href="#character">Character</a>
        <a class = "hover:text-blue-500"href="#staff">Staff</a>
        <a class = "hover:text-blue-500"href="#relations">Relations</a>
    </div>

    <section id="details" class="flex flex-col items-center justify-center max-w-4xl mx-auto mt-10  ">
       <h3 class="text-xl font-bold text-gray-500 mb-1" >Details</h3>
       <div class="w-full flex flex-row justify-evenly border-2 border-blue-600 rounded-xl  px-4 py-4 ">
        <div class="data-column">
            <div class="data-cell">
                <p class="font-bold">Format</p>
                <p>{{animeState.property.format || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Studio</p>
                <div v-if="animeState.property.studios" class="flex flex-col">
                    <RouterLink class="hover:text-blue-600" v-for="item in animeState.property.studios " :key="item.id" :to="`/studio/${item.studio.id}/`">{{ item.studio.name || 'Studio name' }}</RouterLink>
                </div>
                <p v-else>'No info'</p>
                
            </div>
            <div class="data-cell">
                <p class="font-bold">Source</p>
                <p>{{animeState.property.source || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Episodes</p>
                <p>{{animeState.property.episodes || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Duration</p>
                <p>{{animeState.property.duration || 'No info'}}</p>
            </div>
        </div>
        <div class="data-column">
            <div class="data-cell">
                <p class="font-bold">Anilist Score</p>
                <p>{{animeState.property.anilist_score || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Mean Score</p>
                <p>{{animeState.property.mean_score || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Status</p>
                <p>{{animeState.property.status || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Start Date</p>
                <p>{{animeState.property.start_date || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">End date</p>
                <p>{{animeState.property.end_date || 'No info'}}</p>
            </div>
        </div>           
        <div class="data-column">
            <div class="data-cell">
                <p class="font-bold">Romanji Title</p>
                <p>{{animeState.property.romaji_title || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">English Title</p>
                <p>{{animeState.property.english_title || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p class="font-bold">Native Title</p>
                <p>{{animeState.property.native_title || 'No info'}}</p>
            </div>
        </div>  
       </div>
        
    </section>

    <section id="character" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center">
        <h3 class="text-xl font-bold text-gray-500 mb-1">Character</h3>
        <div id="character-frame" v-if="animeState.property.characters" class="grid grid-cols-2 w-full border-2 border-blue-600 rounded-xl px-4 py-4 " >
            <div v-for="item in animeState.property.characters" :key="item.id" class="flex flex-row">
                <CharacterCard v-if="item.character" :character="item.character"></CharacterCard>
                <div>
                    <p>{{ item.char_role || 'No role Info'}}</p>
                    <p>Voice Actor <i class="pi pi-arrow-right"></i></p>
                </div>
                <StaffCard v-if="item.staff" :staff="item.staff"></StaffCard>
            </div>
        </div>
        <div v-else>There is no information about character of this anime</div>
    </section>
    

    <section id="staff" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center">
        <h3 class="text-xl font-bold text-gray-500 mb-1">Staff</h3>
        <div id="staff-frame" v-if="animeState.property.staffs" class="grid grid-cols-2 w-full border-2 border-blue-600 rounded-xl px-4 py-4 " >
            <div v-for="item in animeState.property.staffs" :key="item.id" class="flex flex-row">
                <StaffCard v-if="item.staff" :staff="item.staff"></StaffCard>
                <p>{{ item.staff_role || 'No role Info'}}</p>
            </div>
        </div>
    </section>


    <section id="relations" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center">
        <h3 class="text-xl font-bold text-gray-500 mb-1">Relations</h3>
        <div id="relation-frame" v-if="animeState.property.relations" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <div v-for="item in animeState.property.relations" :key="item.id" class="flex flex-col max-w-40 justify-center items-center">
                <AnimeCardURL v-if="item.anime.url" :url="item.anime.url"></AnimeCardURL>
                <p>{{ item.relation || 'No role Info'}}</p>
            </div>
        </div>
    </section>
</template>