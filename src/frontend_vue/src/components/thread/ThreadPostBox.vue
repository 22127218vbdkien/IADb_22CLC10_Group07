<script setup>
import { userState } from '@/store/userStore';
import { reactive } from 'vue';
import { userState } from '@/store/userStore';
import { useRouter } from 'vue-router';
import axios from 'axios';


const stateAuth = userState()

const formInfo = reactive({
    title: "",
    body:"",
    
})


const validate = () => {
    if (formInfo.title.length <= 0 || formInfo.body.length <= 0){
        alert('Please complete the form')
        return false
    }
    return true
}

const handlePostThread = async () => {
    const status = validate()
    if (status){
        try{
            const response = await axios.post('/api/threads/', formInfo, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization" : `token ${stateAuth.userAuth.token}`
                }
            })

        }catch(error){
            console.log(error)
        }
    }
}
</script>

<template>


</template>