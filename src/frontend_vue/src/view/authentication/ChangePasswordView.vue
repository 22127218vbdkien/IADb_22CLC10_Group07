<script setup>
import { userState } from '@/store/userStore';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';
import router from '@/router';
const _router = useRouter()
const formInfo = reactive({
    old_password: null,
    new_password: null
})

const stateAuth = userState()


const handleChangePassword = async () => {
    if (!stateAuth.isAuthenticated )
        alert('User is not logged in or missing credentials. Please log in!')    
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.post('/api/user/changePassword/', formInfo, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            // if (response.status)
            //     alert('Already in favorites')
        }catch(error){
            console.log(error)
            alert('Wrong old password!!! Please check your infomation')
        }
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
    }
}

</script>

<template>

<div>
    <form>
        <div>
            <label for="old_password">Old password</label>
            <input type="password" name="old_password" id="old_password" v-model="formInfo.old_password">
        </div>
        <div>
            <label for="new_password">New password</label>
            <input type="password" name="new_password" id="new_password" v-model="formInfo.new_password">
        </div>
        <button type="submit" @click.prevent="handleChangePassword">Submit</button>
    </form>

</div>

</template>