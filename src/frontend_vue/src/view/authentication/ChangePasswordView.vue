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
            if (response.ok || response.status === 200 ||response.status === 204 ||response.status === 201 ||response.status === 202 )
                alert('Change password successfully')
                stateAuth.logout(_router)
            //     alert('Already in favorites')
        }catch(error){
            alert('Wrong old password!!! Please check your infomation')
        }
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
    }
}

</script>

<template>
    <section class="bg-blue-100">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="flex flex-col items-center bg-white w-full max-w-2xl py-4 rounded-3xl shadow-lg">
                <h1 class="text-xl text-center font-bold leading-tight tracking-tight text-gray-900 md:text-2xl mb-4">
                    Change your password
                </h1>
                <form class="space-y-4 md:space-y-6 max-w-3xl">
                    <div>
                        <label for="old_password" class="font-semibold block mb-1 text-sm  text-gray-900">Old password</label>
                        <input class="border rounded-xl w-full text-base px-2 py-1 
                        focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" type="password" name="old_password" id="old_password" v-model="formInfo.old_password">
                    </div>
                    <div>
                        <label for="new_password" class="font-semibold block mb-1 text-sm  text-gray-900">New password</label>
                        <input class="border rounded-xl w-full text-base px-2 py-1 
                        focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" type="password" name="new_password" id="new_password" v-model="formInfo.new_password">
                    </div>
                    <button class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                    font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" type="submit" @click.prevent="handleChangePassword">Submit ( •̀ ω •́ )✧</button>
                </form>
            </div>
        </div>
    </section>
</template>