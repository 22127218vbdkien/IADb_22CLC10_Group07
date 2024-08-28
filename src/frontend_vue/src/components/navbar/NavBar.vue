<script setup>
    import { RouterLink, useRouter } from 'vue-router';
    import { userState } from '@/store/userStore';
    const stateAuth = userState()
    const _router = useRouter()
</script>

<template>
    <nav class="w-full">
        <RouterLink to="/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">To home</RouterLink>
        <RouterLink to="/animes/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Animes</RouterLink>
        <RouterLink v-if="stateAuth.isAuthenticated" to="/forum/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Forum</RouterLink>
        <RouterLink to="/animes/search" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Search Anime</RouterLink>
        <RouterLink to="/characters/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Character</RouterLink>
        <RouterLink to="/staffs/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Staff</RouterLink>
        <RouterLink v-if="!stateAuth.isAuthenticated" to="/login/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Login</RouterLink>
        <div v-if="stateAuth.isAuthenticated" @click="stateAuth.logout(_router)" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Logout</div>
    </nav>
</template>