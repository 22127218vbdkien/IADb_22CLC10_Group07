<script setup>
import { reactive, defineEmits, ref } from 'vue';
import { userState } from '@/store/userStore';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
const stateAuth = userState()
const _router = useRouter()
const _route = useRoute()
const userProfile = defineProps({
    info: Object
}) 

const userProfileNew = reactive({
    data:{
        id: null,
        about: null,
        avatar: null,
        url: null, 
    }
    
})
const avatar = reactive({
    data:""
})
const showImage = ref(false)
const convertToBase64 = (event) =>{
    const reader = new FileReader();
    reader.readAsDataURL(event.target.files[0]);
    reader.onload = () =>{
        avatar.data = reader.result
        showImage.value = true
    }
    
}

const emit = defineEmits(['modal-close'])

const handleChangeAvatar = async () =>{
    
    userProfileNew.data = userProfile.info
    userProfileNew.data.avatar = avatar.data
    try{
        const response = await axios.put(userProfileNew.data.url, 
            userProfileNew.data, {
            headers:{
                "Content-Type":"application/json",
                "Authorization": `token ` + stateAuth.userAuth.token
            }
            })
        if (response.status === 200 || response.status === 201)
            alert('Change suscessfully')
            _router.push('/profile/')
        console.log(response)
    }catch(error){
        console.log(error)
    }
} 
</script>

<template>

    <div class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 
    left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)]
    max-h-full bg-black bg-opacity-60 flex">
        <div class="p-4 w-full max-w-md max-h-full bg-blue-50 mx-auto my-auto top-auto py-4 px-8 rounded">
            <div>
                <h3>Change Avatar</h3>
                <i class="pi pi-times" @click="()=>emit('modal-close')"></i>
            </div>
            <div>
                <input class="block" type="file" accept="image/png, image/jpeg" @change="convertToBase64">
                <img v-if="showImage" :src="avatar.data" alt="New user profile">
            </div>
        <button @click="handleChangeAvatar">Confirm</button>

        </div>
    </div>
</template>