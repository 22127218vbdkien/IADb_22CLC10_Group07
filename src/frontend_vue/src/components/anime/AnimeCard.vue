<script setup>
    import { defineProps, ref } from 'vue';
    import { RouterLink } from 'vue-router';
    const props = defineProps({
        anime:Object
    })
</script>

<template>
    <div class="card-container hover:border-blue-600 hover:border-4 hover:border-dashed w-40 px-1 py-2">
        <RouterLink :to="`/animes/${props.anime.id}/`">
            <div>
            <img :src="anime.cover_img_large" alt="Anime Image"/>
            <div class="text-sm mt-1">{{ anime.romaji_title }}</div>
            </div>
        </RouterLink>
    </div>
</template>


<style scoped>
</style>