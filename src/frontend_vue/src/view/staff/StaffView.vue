<script setup>
import { useRoute, useRouter } from 'vue-router';
import { onMounted, reactive } from 'vue';
import router from '@/router';

import axios from 'axios';
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
    }
    
})

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

</template>