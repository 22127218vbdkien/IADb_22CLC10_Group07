<script setup>
import SearchBar from './SearchBar.vue';
import TagFilter from './TagFilter.vue';
import { onRenderTracked, reactive, ref, watch} from 'vue';
import { onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import PaginationBar from '../PaginationBar.vue';
import axios from 'axios';
import AnimeCard from '../anime/AnimeCard.vue';
import parseParams from '@/searchService/apiSearch';
// Options information
const animeTags = ref([])
const sourceTags = ref([
    {   query: "ORIGINAL",
        name: "Original"}
    , {   query: "MANGA",
        name: "Manga"}
    ,{   query: "LIGHT_NOVEL",
        name: "Light Novel"}
    ,{   query: "VISUAL_NOVEL",
        name: "Visual Novel"}
    ,{   query: "VIDEO_GAME",
        name: "Video Game"}
    ,{   query: "OTHER",
        name: "Other"}
    ,{   query: "NOVEL",
        name: "Novel"}
    ,{   query: "DOUJINSHI",
        name: "Doujinshi"}
    ,{   query: "ANIME",
        name: "Anime"}
    ,{   query: "WEB_NOVEL",
        name: "Web Novel"}
    ,{   query: "LIVE_ACTION",
        name: "LiveAction"}
    ,{   query: "GAME",
        name: "Game"}
    ,{   query: "COMIC",
        name: "Comic"}
    ,{   query: "MULTIMEDIA_PROJECT",
        name: "Multimedia Project"}
    ,{   query: "PICTURE_BOOK",
        name: "Picture Book"}
])
const statusTags = ref([
    {   query: "FINISHED",
        name: "Finished"}
    , {   query: "NOT_YET_RELEASED",
        name: "Not yet released"}
    ,{   query: "RELEASING",
        name: "Releasing"}
    ,{   query: "CANCELLED",
        name: "Cancelled"}
    ,{   query: "HIATUS",
        name: "Hiatus"}
    ])
const formatTags = ref([
{   query: "TV",
        name: "TV"}
    , {   query: "TV_SHORT",
        name: "TV SHORT"}
    ,{   query: "MOVIE",
        name: "Movie"}
    ,{   query: "SPECIAL",
        name: "Special"}
    ,{   query: "OVA",
        name: "OVA"}
    ,{   query: "ONA",
    name: "ONA"}])
const studioTags = ref([])
const orderingTags = ref([
    {
        query: "start_date",
        name: "Start Date - ascending"
    },
    {
        query: "-start_date",
        name: "Start Date - descending"
    },
    {
        query: "popularity",
        name: "Popularity - ascending"
    },
    {
        query: "-popularity",
        name: "Popularity - descending"
    },
    {
        query: "trending",
        name: "Trending - ascending"
    },
    {
        query: "-trending",
        name: "Trending - descending"
    },
    {
        query: "favorites",
        name: "Favorites - ascending"
    },
    {
        query: "-favorites",
        name: "Favorites - descending"
    },
    {
        query: "anilist_score",
        name: "Anilist score - ascending"
    },
    {
        query: "-anilist_score",
        name: "Anilist Date - ascending"
    },

])
onMounted(async () => {
    try{
        let response = await axios.get('/api/tags/')
        animeTags.value = response.data
        console.log(animeTags.value)
        // let next = response.data["next"]
        // while (next != null){
        //     const nextPage = await axios.get(next)
        //     animeTags.value = animeTags.value.concat(response.data["results"])
        // }
    }catch(error){
        console.log(error)
    }
})


onMounted(async () => {
    try{
        const response = await axios.get('/api/studios/')
        studioTags.value = response.data["results"]
    }catch(error){
        console.log(error)
    }
})



onMounted(async () => {
    const query = _route.query
    try{
        const response = await axios.get('/api/animes/', {
            params:query,
            paramsSerializer: (params) => parseParams(params)
        })
        state.page = response.data
        showAnime.value = true

    } catch(error){
        console.log(error)
    }
})
// Query information
const userQuery = reactive({
    content: {
        tags:[],
        anime_format: "",
        status: "",
        source: "",
        studios: [],
        search: "",
        ordering:"",
        page: 1
    },
    limit:5
})

const state = reactive({
    page:{
        count: 0,
        next: "",
        previous: null,
        results:[]
    }
})

const changeTags = (event) => {
    userQuery.content.tags = event
    console.log(event)
}

const chnageFormat = (event) => {
    userQuery.content.anime_format = event
    console.log(event)

}

const changeStatus = (event) => {
    userQuery.content.status = event
    console.log(event)

}
const changeSource = (event) => {
    userQuery.content.source = event
    console.log(event)

}

const changeStudio = (event) => {
    userQuery.content.studios = event
    console.log(event)

}

const changeSearch = (event) => {
    userQuery.content.search = event
    console.log(event)

}

const changeOrdering = (event) => {
    userQuery.content.ordering = event
    console.log(event)

}

const changePage = (event) => {
    userQuery.content.page = event
    _router.push({ path: _route.fullPath, query: userQuery.content })
    console.log(event)

}
// Handle Query

const _route = useRoute()
const _router = useRouter()


const handleQuery = () => {
    userQuery.content.page = 1
    _router.push({ path: _route.fullPath, query: userQuery.content })
}
const showAnime = ref(false)


watch(() => _route.query, async (query) => {
    
    try{
        const response = await axios.get('/api/animes/', {
            params:query,
            paramsSerializer: (params) => parseParams(params)
        })
        state.page = response.data
        showAnime.value = true

    } catch(error){
        console.log(error)
    }}) 


</script>

<template>
    <SearchBar v-on:sendChange="changeSearch" target="Anime" class="px-7"></SearchBar>
    
    <div class="grid grid-cols-4 gap-0 px-7">
        <TagFilter :options="animeTags" filterName="Tag" :isMultiple="true" v-on:changeTagLists="changeTags"></TagFilter>
        <TagFilter :options="statusTags" filterName="Status" :isMultiple="false" v-on:changeTagLists="changeStatus"></TagFilter>
        <TagFilter :options="studioTags" filterName="Studio" :isMultiple="true" v-on:changeTagLists="changeStudio"></TagFilter>
        <TagFilter :options="formatTags" filterName="Format" :isMultiple="false" v-on:changeTagLists="chnageFormat"></TagFilter>
        <TagFilter :options="sourceTags" filterName="Source" :isMultiple="false" v-on:changeTagLists="changeSource"></TagFilter>
        <TagFilter :options="orderingTags" filterName="Ordering" :isMultiple="false" v-on:changeTagLists="changeOrdering"></TagFilter>

    </div>
    
    <div><button @click="handleQuery" class="py-2 px-4 my-2 border-2 border-blue-500 bg-blue-100 rounded-xl hover:bg-blue-300" >Click to Search and filter</button></div>

    <div v-if="showAnime">
        <AnimeCard v-for="item in state.page.results" :anime="item" :key="item.id"></AnimeCard>
    </div>
    <PaginationBar :_limit="userQuery.limit" :_start="userQuery.content.page" v-bind:key="userQuery.content.page" v-on:changePage="changePage"></PaginationBar>
    <!-- <button class="px-2 py-2">Click to search anime</button> -->
</template>