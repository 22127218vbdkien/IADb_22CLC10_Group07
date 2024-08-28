
<script setup>
import { userState } from '@/store/userStore';
import { onMounted, reactive } from 'vue';
import AnimeCard from '@/components/anime/AnimeCard.vue';
import AnimeCardURL from '@/components/anime/AnimeCardURL.vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import CharacterCard from '@/components/character/CharacterCard.vue';
import StaffCard from '@/components/staff/StaffCard.vue';
const _router = useRouter()
const stateAuth = userState()
const userProfile = reactive({
    profile: {
        url: null,
        id: null,
        about: null,
        avatar: null
    }
})

const userCollection = reactive({
    completed:[],
    dropped:[],
    paused:[],
    planning:[],
    watching:[]
})

const userFavorite = reactive({
    anime: [],
    staff: [],
    character: [],
})
onMounted(async () => {
    //Fetch user profile
    if (!stateAuth.isAuthenticated ){
        alert('User is not logged in or missing credentials. Please log in!') 
        _router.push('/')   
    }
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.get('/api/userprofiles/current/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userProfile.profile = response.data
                console.log(response)
        }catch(error){
            console.log(error)
        }
        //Fetch user collection
        try{
            const response = await axios.get('/api/animeincollection/Completed/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userCollection.completed = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        try{
            const response = await axios.get('/api/animeincollection/Dropped/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userCollection.dropped = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        try{
            const response = await axios.get('/api/animeincollection/Paused/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userCollection.paused = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        try{
            const response = await axios.get('/api/animeincollection/Watching/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userCollection.watching = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        //Fetch Favorite
        try{
            const response = await axios.get('/api/animeincollection/Favorite/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userFavorite.anime = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        try{
            const response = await axios.get('/api/favoritecharacters/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userFavorite.character = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        try{
            const response = await axios.get('/api/favoritestaffs/', {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if (response.status === 200)
                userFavorite.staff = response.data['results']
                console.log(response)
        }catch(error){
            console.log(error)
        }
        
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
        _router.push('/')   
    }
})
</script>

<template>
<div>
<h2>userProfile</h2>
<div>
    {{ userProfile }}
</div>
</div>
<div id="collection">
    <h3>Anime in collection</h3>
    <div>
        <h3>Completed</h3>
        <div>
        <AnimeCard v-for="(item, index) in userCollection.completed" :key="index" :anime="item.anime"></AnimeCard>
        </div>
    </div>
    <div>
        <h3>Dropped</h3>
        <div>
        <AnimeCard v-for="(item, index) in userCollection.dropped" :key="index" :anime="item.anime"></AnimeCard>
        </div>
    </div>
    <div>
        <h3>Paused</h3>
        <div>
        <AnimeCard v-for="(item, index) in userCollection.paused" :key="index" :anime="item.anime"></AnimeCard>
        </div>
    </div>
    <div>
        <h3>Planning</h3>
        <div>
        <AnimeCard v-for="(item, index) in userCollection.planning" :key="index" :anime="item.anime"></AnimeCard>
        </div>
    </div>
    <div>
        <h3>Watching</h3>
        <div>
        <AnimeCard v-for="(item, index) in userCollection.watching" :key="index" :anime="item.anime"></AnimeCard>
        </div>
    </div>
</div>

<div id="favorite">
    <h3>Favorite</h3>
    <div>
        <h3>Animes</h3>
        <AnimeCardURL v-for="(item, index) in userFavorite.anime" :key="index" :url="item.anime_id"></AnimeCardURL>
    </div>
    <div>
        <h3>Characters</h3>
        <CharacterCard v-for="(item, index) in userFavorite.character" :key="index" :character="item.character"></CharacterCard>
        
    </div>
    <div>
        <h3>staffs</h3>
        <StaffCard v-for="(item, index) in userFavorite.staff" :key="index" :staff="item.staff"></StaffCard>
    </div>
</div>
</template>


