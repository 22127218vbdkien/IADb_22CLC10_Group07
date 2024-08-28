<script setup>
import { useRoute, useRouter } from 'vue-router';
import { computed, onMounted, reactive } from 'vue';
import router from '@/router';
import { userState } from '@/store/userStore';
import { apiURL } from '@/searchService/apiSearch';
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
    <button @click.prevent="addStaffToFavorite">Add to Favorite</button>

</template>