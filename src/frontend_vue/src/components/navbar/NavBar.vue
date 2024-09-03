<script setup>
    import { RouterLink, useRouter } from 'vue-router';
    import { userState } from '@/store/userStore';
    const stateAuth = userState()
    const _router = useRouter()
</script>

<template>
    <nav class="w-full flex flex-row bg-blue-200">
        <RouterLink to="/" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">To home</RouterLink>
        <RouterLink to="/animes/" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded font-medium">Animes</RouterLink>
        <RouterLink to="/forum/" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">Forum</RouterLink>
        <!-- <RouterLink to="/animes/search" class="px-2 hover:bg-blue-400 cursor-pointer rounded">Search Anime</RouterLink> -->
        <RouterLink to="/characters/" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">Character</RouterLink>
        <RouterLink to="/staffs/" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">Staff</RouterLink>
        <RouterLink v-if="!stateAuth.isAuthenticated" to="/login/" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">Login</RouterLink>
        <RouterLink v-if="stateAuth.isAuthenticated" to="/profile/"  class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">Profile</RouterLink>
        <a v-if="stateAuth.isAuthenticated"  class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium" href="http://127.0.0.1:8000/admin/">To Admin</a>
        <div v-if="stateAuth.isAuthenticated" @click="stateAuth.logout(_router)" class="px-2 py-2 hover:bg-blue-400 cursor-pointer rounded w-fit font-medium">Logout</div>
    </nav>
</template>