<script setup>
    import { RouterLink } from 'vue-router';
</script>

<template>
    <nav>
        <RouterLink to="/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">To home</RouterLink>
        <RouterLink to="/animes/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Animes Browse</RouterLink>
        <RouterLink to="/forum/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Forum</RouterLink>
        <RouterLink to="/login/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Login</RouterLink>
        <RouterLink to="/animes/search" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Search Anime</RouterLink>
        <RouterLink to="/characters/" class="px-2 hover:bg-blue-400 cursor-pointer rounded-xl">Browse Character</RouterLink>
    </nav>
</template>