<script setup>
    import { RouterLink, useRouter } from 'vue-router';
    import { userState } from '@/store/userStore';
    const stateAuth = userState()
    const _router = useRouter()
</script>

<template>
    <nav class="w-full">
        <RouterLink to="/" class="px-2 hover:bg-blue-400 cursor-pointer rounded">To home</RouterLink>
        <RouterLink to="/animes/" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Animes</RouterLink>
        <RouterLink v-if="stateAuth.isAuthenticated" to="/forum/" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Forum</RouterLink>
        <RouterLink to="/animes/search" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Search Anime</RouterLink>
        <RouterLink to="/characters/" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Character</RouterLink>
        <RouterLink to="/staffs/" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Staff</RouterLink>
        <RouterLink v-if="!stateAuth.isAuthenticated" to="/login/" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Login</RouterLink>
        <RouterLink v-if="stateAuth.isAuthenticated" to="/profile/"  class="px-2 hover:bg-blue-400 cursor-pointer rounded">Profile</RouterLink>
        <div v-if="stateAuth.isAuthenticated" @click="stateAuth.logout(_router)" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Logout</div>
    </nav>
</template>