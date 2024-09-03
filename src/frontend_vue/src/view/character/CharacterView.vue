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
        }catch(error){
            alert('Already in favorites')
        }
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
    }
}

const removeCharacterFromFavorite = async () => {
    try{
        const response = await axios.delete(collectionURL.value, {
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        }).catch((error)=>{
            return error.response
        })
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
    
    <section class="flex flex-row max-w-5xl mx-auto mt-10">
        <div class="container w-fit min-w-48 min-h-52 flex flex-col justify-center items-center mr-10">
            <img :src="character.info.img_large" alt="character image" class="w-48 h-64 object-cover">
            <button
                class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
                    hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer"
                v-if="!isInCollection"
                @click.prevent="addCharacterToFavorite">
                Add to Favorite
            </button>
            <button
                class="px-4 py-2 w-56 bg-red-200 text-red-800 border-red-800
                    hover:bg-red-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer"
                v-if="isInCollection"
                @click.prevent="removeCharacterFromFavorite">
                Remove from Favorite
            </button>
        </div>
        <div class="flex flex-col">
            <div class="text-2xl font-bold text-gray-500">
                <p >{{ character.info.name }}</p>
            </div>
            <div>
                <div >

                    {{ character.info.description || 'There is no description' }}

                </div>
            </div>
            <div class="text-red-600 pt-2">
                <i class="pi pi-heart"></i> {{ character.info.favorites || "No info" }}
            </div>
        </div>
    </section>
    
    <br>
    <nav class="w-full flex flex-row justify-evenly items-center border-y-2 border-blue-500 my-5">
        <a class = "hover:text-blue-500" href="#details">Details</a>
        <a class = "hover:text-blue-500" href="#in_animes">In animes</a>
    </nav>
    
    <section id="details" class="flex flex-col items-center justify-center max-w-4xl mx-auto mt-10 ">
        <h3 class="text-xl font-bold text-gray-500 mb-1">Details</h3>
        <div id="detail-frame" class="w-full flex flex-row justify-evenly border-2 border-blue-600 rounded-xl  px-4 py-4">
            <div >
                <p class="font-bold">Native name:</p>
                <p>{{ character.info.name_native ||"No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Gender:</p>
                <p>{{ character.info.gender ||"No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Birthday:</p>
                <p>{{ character.info.date_of_birth || "No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Age:</p>
                <p>{{ character.info.age || "No info" }}</p>
            </div>
    
        </div>
    </section>
    <br>
    <div id="in_animes" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center">
        <div class="text-xl font-bold text-gray-500 mb-1">In animes</div>
        <div id="anime-frame" v-if="character.info.in_animes.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <div v-for="(item,index) in character.info.in_animes" :key="index" class="flex flex-col max-w-40 justify-center items-center">
                <AnimeCard :anime="item.anime"></AnimeCard>
                <p>{{ item.char_role || "Role info" }}</p>
            </div>
        </div>
        <div v-else>There is no infomation of animes having this character</div>
    </div>
    
</template>