<script setup>
import { useRoute, useRouter } from 'vue-router';
import router from '@/router';
import { onMounted, reactive, computed} from 'vue';
import axios from 'axios';
import { userState } from '@/store/userStore';
import { apiURL } from '@/searchService/apiSearch';
const _route = useRoute()
const _router = useRouter()
const char_id = _route.params.id
const stateAuth = userState()

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
    },
    url: computed(() => {
                        return apiURL() + `/characters/${char_id}/`
                    }) 
})

const addCharacterToFavorite = async () => {
    if (!stateAuth.isAuthenticated )
        alert('User is not logged in or missing credentials. Please log in!')    
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.post('/api/favoritecharacters/', 
                {
                    char_id: character.url
                }, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            // if (response.status)
            //     alert('Already in favorites')
            console.log(response.status)
        }catch(error){
            alert('Already in favorites')
        }
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
    }
}
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
    <button @click.prevent="addCharacterToFavorite">Add to Favorite</button>
</template>