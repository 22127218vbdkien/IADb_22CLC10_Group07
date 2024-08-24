<script setup>
import SearchBar from './SearchBar.vue';
import TagFilter from './TagFilter.vue';
import { reactive, ref } from 'vue';
import { onMounted } from 'vue';
import axios from 'axios';
const animeTags = ref([])
const sourceTags = ref([
    {   query: "Original",
        name: "Original"}
    , {   query: "Manga",
        name: "Manga"}
    ,{   query: "Light_Novel",
        name: "Light Novel"}
    ,{   query: "Visual_Novel",
        name: "Visual Novel"}
    ,{   query: "Video_Game",
        name: "Video Game"}
    ,{   query: "Other",
        name: "Other"}
    ,{   query: "Novel",
        name: "Novel"}
    ,{   query: "Doujinshi",
        name: "Doujinshi"}
    ,{   query: "Anime",
        name: "Anime"}
    ,{   query: "Web_Novel",
        name: "Web Novel"}
    ,{   query: "Live_Action",
        name: "LiveAction"}
    ,{   query: "Game",
        name: "Game"}
    ,{   query: "Comic",
        name: "Comic"}
    ,{   query: "Multimedia_Project",
        name: "Multimedia Project"}
    ,{   query: "Picture_Book",
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
onMounted(async () => {
    try{
        let response = await axios.get('/api/tags/')
        animeTags.value = animeTags.value.concat(response.data["results"])
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
</script>

<template>
    <SearchBar target="Anime" class="px-7"></SearchBar>
    
    <div class="grid grid-cols-5 gap-0 px-7">
        <TagFilter :options="animeTags" filterName="Tag"></TagFilter>
        <TagFilter :options="statusTags" filterName="Status"></TagFilter>
        <TagFilter :options="studioTags" filterName="Studio"></TagFilter>
        <TagFilter :options="formatTags" filterName="Format"></TagFilter>
        <TagFilter :options="sourceTags" filterName="Source"></TagFilter>
    </div>
 

    <!-- <button class="px-2 py-2">Click to search anime</button> -->
</template>