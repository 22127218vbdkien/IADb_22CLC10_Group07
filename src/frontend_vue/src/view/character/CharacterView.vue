<script setup>
import { useRoute, useRouter } from 'vue-router';
import router from '@/router';
import { onMounted, reactive } from 'vue';
import axios from 'axios';
const _route = useRoute()
const _router = useRouter()
const char_id = _route.params.id

const character = reactive({
    info : {
        id: 0,
        name: "",
        name_native: "",
        img_large:  "",
        img_med: "",
        description: "",
        gender: "",
        date_of_birth:"",
        age: "",
        favorites: 0,
        in_animes:[],
    }
    
})

onMounted(async () => {
    try{
        const response = await axios.get(`/api/characters/${char_id}/`)
        character.info = response.data
        console.log(character.info) 
    }catch(error){
        console.log(error)
    }
})
</script>

<template>
    <img :src="character.info.img_large" alt="character image">
    <p>{{ character.info.name }}</p>
    
</template>