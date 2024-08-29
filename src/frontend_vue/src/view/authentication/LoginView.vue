<script setup>
import { defineProps } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';
import { userState } from '@/store/userStore';
import axios from 'axios';
const user = reactive({
    username : "",
    password : "",
    error: ""
})
const _router = useRouter()
const stateAuth = userState()

const submitLogin = async () =>{
    await stateAuth.login(user.username, user.password, _router)
    if (! stateAuth.isAuthenticated){
        user.error = 'Login failed. Please check your credentials.'
    }
}

const resetError = () =>{
    user.error = ""
}
</script>

<template>

    <section class="bg-blue-100">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="flex flex-col items-center bg-white w-full max-w-2xl py-4 rounded-3xl shadow-lg">
                <h1 class="text-xl text-center font-bold leading-tight tracking-tight text-gray-900 md:text-2xl mb-4">
                  Sign in to your account
                </h1>
                <form class="space-y-4 md:space-y-6 max-w-3xl">
                    <div>
                        <label for="username" class="font-semibold block mb-1 text-sm  text-gray-900">Username</label>
                        <input class="border rounded-xl w-full text-base px-2 py-1 
                        focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600"type="text" id="username" placeholder="..." v-model="user.username" @input="resetError"/>
                    </div>
                    <div>
                        <label for="password" class="font-semibold block mb-1 text-sm  text-gray-900">Password</label>
                        <input class="border rounded-xl w-full text-base px-2 py-1 
                        focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600"type="password" id="password" placeholder="..." v-model="user.password" @input="resetError"/>
                    </div>

                    <button class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                     font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" @click.prevent = "submitLogin" >Sign In ( •̀ ω •́ )✧</button>
                </form>
                <RouterLink class="mt-2 text-gray-600 hover:text-blue-500 hover:cursor-pointer" to="/signup/">Create a new account <i class="pi pi-arrow-right"></i></RouterLink>
            </div>
            
        </div>
    </section>

</template>