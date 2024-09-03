
<script setup>
import { userState } from '@/store/userStore';
import { onMounted, reactive, ref } from 'vue';
import AnimeCard from '@/components/anime/AnimeCard.vue';
import AnimeCardURL from '@/components/anime/AnimeCardURL.vue';
import { useRoute, useRouter, RouterLink} from 'vue-router';
import axios from 'axios';
import CharacterCard from '@/components/character/CharacterCard.vue';
import StaffCard from '@/components/staff/StaffCard.vue';
import userProfileUpdateForm from '@/components/popup/userProfileUpdateForm.vue';
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
            if (response.status === 200){
                userProfile.profile = response.data
                const response_next = await axios.get(userProfile.profile.url, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
                if (response_next.status === 200){
                     userProfile.profile = response_next.data
                }
            }
                
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
        }catch(error){
            console.log(error)
        }
        
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
        _router.push('/')   
    }
})

const isChangingAvatar = ref(false)
const toggleChangeAvatar = () =>{
    isChangingAvatar.value = !isChangingAvatar.value
}

const handleRemoveAvatar = async () => {
    userProfile.profile.avatar = null
    try{
        const response = await axios.put(userProfile.profile.url, 
            userProfile.profile, {
            headers:{
                "Content-Type":"application/json",
                "Authorization": `token ` + stateAuth.userAuth.token
            }
            })
        if (response.status === 200 || response.status === 201){
            alert('Change suscessfully')
            _router.push('/profile/')
        }
    }catch(error){
        console.log(error)
    }
}
</script>

<template>

<section id="user-profile" class="flex flex-col justify-center items-center max-w-5xl mx-auto mt-10">
    <div id="user-avatar" class="container w-fit min-w-32 min-h-40 flex flex-col justify-center items-center ">
        <h2 class="text-xl font-bold text-gray-500 mb-1">Profile</h2>
        <img class="max-h-32" v-if="userProfile.profile.avatar" :src="`${userProfile.profile.avatar}`" alt="userAvatar">
        <img class="max-h-32" v-else src="../assets/default_ava.png"  alt="default Avatar">
    </div>
    <div class="flex flex-col justify-center items-center">
        <h3 class="text-xl font-bold text-gray-500 mb-1">Option</h3>
        <button class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
        hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer" @click="toggleChangeAvatar">Change Avatar</button>
        <button class="px-4 py-2 w-56 bg-red-200 text-red-800 border-red-800
        hover:bg-red-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer" @click="handleRemoveAvatar">Remove Avatar</button>
        <RouterLink to="/change-password/" class="px-4 py-2 w-56 bg-green-200 text-green-800 border-green-800
        hover:bg-green-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer">Change your password</RouterLink>
    </div>
    
</section>
<div id="new-avatar">
    <userProfileUpdateForm v-if="isChangingAvatar" @modal-close="toggleChangeAvatar" :info="userProfile.profile"></userProfileUpdateForm>
</div>

<nav class="w-full flex flex-row justify-evenly items-center border-y-2 border-blue-500 my-5">
    <a href="#collection">Collection</a>
    <a href="#favorite">Favorite</a>
</nav>


    <section id="collection" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center border-blue-600 border-dashed border-2 rounded-xl px-4 py-4  ">
        <h3 class="text-2xl font-bold text-gray-500 mb-1">Anime in collection</h3>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Completed</h3>
            <div v-if="userCollection.completed.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
                <AnimeCard v-for="(item, index) in userCollection.completed" :key="index" :anime="item.anime"></AnimeCard>
            </div>
            <div v-else>There is no info</div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Dropped</h3>
            <div v-if="userCollection.dropped.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <AnimeCard v-for="(item, index) in userCollection.dropped" :key="index" :anime="item.anime"></AnimeCard>
            </div>
            <div v-else>There is no info</div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Paused</h3>
            <div v-if="userCollection.paused.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <AnimeCard v-for="(item, index) in userCollection.paused" :key="index" :anime="item.anime"></AnimeCard>
            </div>
            <div v-else>There is no info</div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Planning</h3>
            <div v-if="userCollection.planning.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <AnimeCard v-for="(item, index) in userCollection.planning" :key="index" :anime="item.anime"></AnimeCard>
            </div>
            <div v-else>There is no info</div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Watching</h3>
            <div v-if="userCollection.watching.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <AnimeCard v-for="(item, index) in userCollection.watching" :key="index" :anime="item.anime"></AnimeCard>
            </div>
            <div v-else>There is no info</div>
        </div>
    </section>

    <section id="favorite" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center  border-blue-600 border-dashed border-2 rounded-xl px-4 py-4  ">
        <h3 class="text-xl font-bold text-gray-500 mb-1" >Favorite</h3>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Animes</h3>
            <div v-if="userFavorite.anime.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
                <AnimeCardURL v-for="(item, index) in userFavorite.anime" :key="index" :url="item.anime_id"></AnimeCardURL>
            </div>
            <div v-else>There is no info</div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Characters</h3>
            <div v-if="userFavorite.character.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
                <CharacterCard v-for="(item, index) in userFavorite.character" :key="index" :character="item.character"></CharacterCard>
            </div>
            
            <div v-else>There is no info</div>
        </div>
        <div class="flex flex-col items-center justify-center">
            <h3 class="text-xl font-bold text-gray-500 mb-1">Staffs</h3>
            <div v-if="userFavorite.staff.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
                <StaffCard v-for="(item, index) in userFavorite.staff" :key="index" :staff="item.staff"></StaffCard>
            </div>
            <div v-else>There is no info</div>
        </div>
    </section>
</template>


