<script setup>
import { useRoute, useRouter } from 'vue-router';
import router from '@/router';
import { onMounted, reactive, computed, ref} from 'vue';
import axios from 'axios';
import { userState } from '@/store/userStore';
import { apiURL } from '@/searchService/apiSearch';
import AnimeCard from '@/components/anime/AnimeCard.vue';
import CharacterCard from '@/components/character/CharacterCard.vue';
const _route = useRoute()
const _router = useRouter()
const char_id = _route.params.id
const stateAuth = userState()
const isInCollection = ref(false)
const collectionURL = ref("")
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

const removeCharacterFromFavorite = async () => {
    console.log(collectionURL)
    try{
        const response = await axios.delete(collectionURL.value, {
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        }).catch((error)=>{
            return error.response
        })
        console.log(response)
        if (response.status === 200 || response.status === 204 || response.status === 202){
            alert('Remove successfuly')
            isInCollection.value = false
            collectionURL.value = ""
        }
    }catch(error){
        console.log(error)
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
    try{
        const response = await axios.get('/api/favoritecharacters/', {
            params: {
                search: character.info.id
            },
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        }).catch((error)=>{
            return error.response
        })
        console.log(response)
        if (response.status === 200){
            if (response.data['count'] > 0){
                isInCollection.value = true
                collectionURL.value = response.data['results'][0].url
            }
        }
    }catch(error){
        console.log(error)
    }
})



</script>

<template>
    <img :src="character.info.img_large" alt="character image">
    <p>{{ character.info.name }}</p>
    <div class="text-red-600"><i class="pi pi-heart"></i>{{ character.info.favorites || "No info" }}</div>
    <button v-if="!isInCollection" @click.prevent="addCharacterToFavorite">Add to Favorite</button>
    <button v-if="isInCollection" @click.prevent="removeCharacterFromFavorite">Remove from Favorite</button>

    <nav>
        <a href="#details">Details</a>
        <a href="#in_animes">In animes</a>
    </nav>
    
    <div id="details">
        <div id="detail-frame">
            <p><span>Gender: </span> {{ character.info.gender ||"No info" }}</p>
            <div>

                <div>Description</div>

                <div >

                    {{ character.info.description || 'There is no description' }}

                </div>
            </div>
            <p><span>Birthday: </span> {{ character.info.date_of_birth || "No info" }}</p>
            <p><span>Age: </span> {{ character.info.age || "No info" }}</p>
        </div>
    </div>
    
    <div id="in_animes">
        <div>In animes</div>
        <div id="anime-frame" v-if="character.info.in_animes.length > 0">
            <div v-for="(item,index) in character.info.in_animes" :key="index">
                <AnimeCard :anime="item.anime"></AnimeCard>
                <p>{{ item.char_role || "Role info" }}</p>
            </div>
        </div>
        <div v-else>There is no infomation of animes having this character</div>
    </div>
    
</template>