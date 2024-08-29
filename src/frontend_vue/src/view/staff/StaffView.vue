<script setup>
import { useRoute, useRouter } from 'vue-router';
import { computed, onMounted, reactive, ref } from 'vue';
import router from '@/router';
import { userState } from '@/store/userStore';
import { apiURL } from '@/searchService/apiSearch';
import CharacterCard from '@/components/character/CharacterCard.vue';
import AnimeCard from '@/components/anime/AnimeCard.vue';
import axios from 'axios';
const stateAuth = userState()
const _route = useRoute()
const _router = useRouter()
const staff_id = _route.params.id
const isInCollection = ref(false)
const collectionURL = ref("")

const staff = reactive({
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
        home_town: "",
        favorites: 0,
        staff_roles:[],
        voiced_characters:[],
    },
    url: computed(() => {
                        return apiURL() + `/staffs/${staff_id}/`
                    }) 

    
})

const addStaffToFavorite = async () => {
    if (!stateAuth.isAuthenticated )
        alert('User is not logged in or missing credentials. Please log in!')    
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.post('/api/favoritestaffs/', 
                {
                    staff_id: staff.url
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

const removeStaffFromFavorite = async () => {
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
        const response = await axios.get(`/api/staffs/${staff_id}/`)
        staff.info = response.data
        console.log(staff.info) 
    }catch(error){
        console.log(error)
    }
    try{
        const response = await axios.get('/api/favoritestaffs/', {
            params: {
                search: staff.info.id
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

    <section id="image-and-description" class="flex flex-row max-w-5xl mx-auto mt-10">
        <div class="container w-fit min-w-48 min-h-52 flex flex-col justify-center items-center mr-10">
            <img :src="staff.info.img_large" alt="staff image">
            <button v-if="!isInCollection" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
                    hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer" @click.prevent="addStaffToFavorite">Add to Favorite</button>
            <button v-if="isInCollection" class="px-4 py-2 w-56 bg-red-200 text-red-800 border-red-800
                    hover:bg-red-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer" @click.prevent="removeStaffFromFavorite">Remove from Favorite</button>
        </div>
        <div class="anime-description flex flex-col ">
            <div class="text-2xl font-bold text-gray-500">
                <p>{{ staff.info.name }}</p>
            </div>
               
                <div >
                    {{ staff.info.description || 'There is no description' }}
                </div>
                <div class="text-red-600"><i class="pi pi-heart"></i>{{ staff.info.favorites || "No info" }}</div>
        </div>
    </section>
    
    
    <nav class="w-full flex flex-row justify-evenly items-center border-y-2 border-blue-500 my-5">
        <a  class = "hover:text-blue-500" href="#details">Details</a>
        <a  class = "hover:text-blue-500" href="#staff-roles">Roles</a>
        <a  class = "hover:text-blue-500" href="#voiced_characters">Voiced Characters</a>
    </nav>

    <section id="details"class="flex flex-col items-center justify-center max-w-4xl mx-auto mt-10 ">
        <h3 class="text-xl font-bold text-gray-500 mb-1">Details</h3>
        <div id="detail-frame" class="w-full flex flex-row justify-evenly border-2 border-blue-600 rounded-xl  px-4 py-4">
            <div >
                <p class="font-bold">Native name:</p>
                <p>{{ staff.info.name_native ||"No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Gender:</p>
                <p>{{ staff.info.gender ||"No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Birthday:</p>
                <p>{{ staff.info.date_of_birth || "No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Age:</p>
                <p>{{ staff.info.age || "No info" }}</p>
            </div>
            <div>
                <p class="font-bold">Hometown:</p>
                <p>{{ staff.info.home_town || "No info" }}</p>
            </div>
        </div>
    </section>


    <section id="staff-roles" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center">
        <div class="text-xl font-bold text-gray-500 mb-1" >Roles</div>
        <div id="role-frame" v-if="staff.info.staff_roles.length > 0" class="grid grid-cols-5 w-full border-2 border-blue-600 rounded-xl px-4 py-4 ">
            <div v-for="(item, index) in staff.info.staff_roles" :key="index" class="flex flex-col max-w-40 justify-center items-center">
                <AnimeCard :anime="item.anime"></AnimeCard>
                <div>{{ item.staff_role || "Staff role" }}</div>
            </div>
        </div>
        <div v-else>This staff has no roles in anime</div>

    </section>

    <section id="voiced_characters" class="max-w-4xl mx-auto mt-10 flex flex-col items-center justify-center">
        <div class="text-xl font-bold text-gray-500 mb-1">Voiced Characters</div>
        <div id="character-frame" v-if="staff.info.voiced_characters.length > 0" class="grid grid-cols-2 w-full border-2 border-blue-600 rounded-xl px-4 py-4 " >
            <div v-for="(item, index) in staff.info.voiced_characters" :key="index" class="flex flex-row" >
                <div>
                    <CharacterCard :character="item.character"></CharacterCard>
                </div>
                <p>{{ item.char_role || "Char role" }}</p>
                <div>
                    <AnimeCard :anime="item.anime"></AnimeCard>
                </div>
            </div>
        </div>
        <div v-else>This staff has not voiced any characters</div>

    </section>
</template>