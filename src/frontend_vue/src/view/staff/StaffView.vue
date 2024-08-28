<script setup>
import { useRoute, useRouter } from 'vue-router';
import { computed, onMounted, reactive } from 'vue';
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

onMounted(async () => {
    try{
        const response = await axios.get(`/api/staffs/${staff_id}/`)
        staff.info = response.data
        console.log(staff.info) 
    }catch(error){
        console.log(error)
    }
})
</script>

<template>
    <div>
        <img :src="staff.info.img_large" alt="staff image">
        <p>{{ staff.info.name }}</p>
    </div>
    <div class="text-red-600"><i class="pi pi-heart"></i>{{ staff.info.favorites || "No info" }}</div>
    <button @click.prevent="addStaffToFavorite">Add to Favorite</button>
    
    <nav>
        <a href="#details">Details</a>
        <a href="#staff-roles">Roles</a>
        <a href="#voice-characters">Voiced Characters</a>
    </nav>

    <div id="details">
        <div id="detail-frame">
            <p><span>Gender: </span> {{ staff.info.gender ||"No info" }}</p>
            <div>

                <div>Description</div>

                <div >

                    {{ staff.info.description || 'There is no description' }}

                </div>
            </div>
            <p><span>Birthday: </span> {{ staff.info.date_of_birth || "No info" }}</p>
            <p><span>Age: </span> {{ staff.info.age || "No info" }}</p>
            <p><span>Hometown: </span> {{ staff.info.home_town || "No info" }}</p>
        </div>
    </div>


    <div id="staff-roles">
        <div>Roles</div>
        <div id="role-frame" v-if="staff.info.staff_roles.length > 0">
            <div v-for="(item, index) in staff.info.staff_roles" :key="index">
                <AnimeCard :anime="item.anime"></AnimeCard>
                <div>{{ item.staff_role || "Staff role" }}</div>
            </div>
        </div>
        <div v-else>This staff has no roles in anime</div>

    </div>

    <div id="voiced_characters">
        <div>Voiced Characters</div>
        <div id="character-frame" v-if="staff.info.voiced_characters.length > 0">
            <div v-for="(item, index) in staff.info.voiced_characters" :key="index">
                <div>
                    <CharacterCard :character="item.character"></CharacterCard>
                    <div>{{ item.char_role || "Char role" }}</div>
                    
                </div>
                <div>
                    <AnimeCard :anime="item.anime"></AnimeCard>
                </div>
            </div>
        </div>
        <div v-else>This staff has not voiced any characters</div>

    </div>
</template>