<script setup>
    import router from '@/router';
    import { RouterLink,  useRoute, useRouter} from 'vue-router';
    import {ref, onMounted, reactive } from 'vue';
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

    const toggleCollectionForm = () =>{
        showform.value = !showform.value
    }
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
            <div v-if="stateAuth.isAuthenticated" class="px-4 py-2 bg-blue-200 text-blue-800 border-blue-800
             hover:bg-blue-400 max-w-max rounded-xl border-2" @click="toggleCollectionForm">Add to list</div>
        </div>

        <div class="container" id="tag_and_description">
            <div>
                <p>{{ animeState.property.romaji_title}}</p>
            </div>
        </div>
    </div>
    <div id="anime-description">
        <div id="description">{{ animeState.property.description || "This anime has no description" }}</div>
        <div id="favorites" class="text-red-600"><i class="pi pi-heart px-1"></i>{{ animeState.property.favorites || 'No info' }}</div>
        <div id="tag-frame" v-if="animeState.property.tags">
            <Tag v-for="item in animeState.property.tags" :key="item.id" :tag="item.tag"></Tag>
        </div>
    </div>
    <animeCollectionForm v-if="showform" :anime_id="Number(_animeid)" @modal-close="toggleCollectionForm"></animeCollectionForm>

    <div>
        <a href="#details">Details</a>
        <a href="#character">Character</a>
        <a href="#staff">Staff</a>
        <a href="#relations">Relations</a>
        <a href="#reccomendation">reccomendation</a>
    </div>

    <div id="details">
       <h3>Details</h3>
        <div class="data-column">
            <div class="data-cell">
                <p>Format</p>
                <p>{{animeState.property.format || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Studio</p>
                <div v-if="animeState.property.studios">
                    <RouterLink class="hover:text-blue-600" v-for="item in animeState.property.studios " :key="item.id" :to="`/studio/${item.studio.id}/`">{{ item.studio.name || 'Studio name' }}</RouterLink>
                </div>
                <p v-else>'No info'</p>
                
            </div>
            <div class="data-cell">
                <p>Source</p>
                <p>{{animeState.property.source || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Episodes</p>
                <p>{{animeState.property.episodes || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Duration</p>
                <p>{{animeState.property.duration || 'No info'}}</p>
            </div>
        </div>
        <div class="data-column">
            <div class="data-cell">
                <p>Average Score</p>
                <p>{{animeState.property.mean_score || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Mean Score</p>
                <p>{{animeState.property.mean_score || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Status</p>
                <p>{{animeState.property.status || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Start Date</p>
                <p>{{animeState.property.start_date || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>End date</p>
                <p>{{animeState.property.end_date || 'No info'}}</p>
            </div>
        </div>           
        <div class="data-column">
            <div class="data-cell">
                <p>Romanji Title</p>
                <p>{{animeState.property.romaji_title || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>English Title</p>
                <p>{{animeState.property.english_title || 'No info'}}</p>
            </div>
            <div class="data-cell">
                <p>Native Title</p>
                <p>{{animeState.property.native_title || 'No info'}}</p>
            </div>
        </div>  
    </div>

    <div id="character">
        <h3>Character</h3>
        <div id="character-frame" v-if="animeState.property.characters" >
            <div v-for="item in animeState.property.characters" :key="item.id">
                <CharacterCard v-if="item.character" :character="item.character"></CharacterCard>
                <StaffCard v-if="item.staff" :staff="item.staff"></StaffCard>
                <p>{{ item.char_role || 'No role Info'}}</p>
            </div>
        </div>
        <div v-else>There is no information about character of this anime</div>
    </div>
    

    <div id="staff">
        <h3>Staff</h3>
        <div id="staff-frame" v-if="animeState.property.staffs">
            <div v-for="item in animeState.property.staffs" :key="item.id">
                <StaffCard v-if="item.staff" :staff="item.staff"></StaffCard>
                <p>{{ item.staff_role || 'No role Info'}}</p>
            </div>
        </div>
    </div>


    <div id="relations">
        <h3>Relations</h3>
        <div id="relation-frame" v-if="animeState.property.relations">
            <div v-for="item in animeState.property.relations" :key="item.id">
                <AnimeCardURL v-if="item.anime.url" :url="item.anime.url"></AnimeCardURL>
                <p>{{ item.relation || 'No role Info'}}</p>
            </div>
        </div>
    </div>
</template>