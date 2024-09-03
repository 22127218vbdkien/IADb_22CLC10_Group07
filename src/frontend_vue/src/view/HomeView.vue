<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { userState } from '@/store/userStore';
const stateAuth = userState()

</script>

<template>

   
    <section id="gretting" class="flex flex-col justify-center items-center max-w-5xl mx-auto mt-10">
        <div v-if="stateAuth.isAuthenticated" class="container w-fit min-w-48 min-h-52 flex flex-col justify-center items-center ">
            <img src="../assets/default_ava.png" alt="Fit Girl" class="mb-4">
            <h1 class="text-2xl font-bold text-gray-500">Welcome back my friend ( •̀ ω •́ )✧</h1>
        </div>
        <div v-else class="container w-fit min-w-48 min-h-52 flex flex-col justify-center items-center">
            <img src="../assets/default_ava.png" alt="Fit Firl" class="mb-4">
            <h1 class="text-2xl font-bold text-gray-500">Greeting visitors ( •̀ ω •́ )✧</h1>
            <RouterLink to="/signup/" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
            hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer">Become our member <i class="pi pi-arrow-right"></i></RouterLink>
        </div>
    </section>
    <section id="navigation" class="flex flex-col justify-center items-center max-w-5xl mx-auto mt-10">
        <h1 class="text-2xl font-bold text-gray-500">Start browsing on IADb today ( •̀ ω •́ )✧</h1>

        <div class="grid grid-cols-2 max-w-5xl gap-x-8 gap-y-4 grid-flow-row">
            <RouterLink to="/animes/" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
            hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer">Browse Anime <i class="pi pi-arrow-right"></i></RouterLink>
            <RouterLink to="/characters/" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
            hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer">Browse Character <i class="pi pi-arrow-right"></i></RouterLink>
            <RouterLink to="/staffs/" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
            hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer">Browse Staff <i class="pi pi-arrow-right"></i></RouterLink>
            <RouterLink  to="/forum/" class="px-4 py-2 w-56 bg-blue-200 text-blue-800 border-blue-800
            hover:bg-blue-400 max-w-80 rounded-xl border-2 text-center mt-2 hover:cursor-pointer">Browse Forum <i class="pi pi-arrow-right"></i></RouterLink>
        </div>
    </section>
    
</template>