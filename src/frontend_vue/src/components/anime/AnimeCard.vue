<script setup>
    import { defineProps, ref } from 'vue';
    import { RouterLink } from 'vue-router';
    const props = defineProps({
        anime:Object
    })
</script>

<template>
    <div>
        <RouterLink :to="`/animes/${props.anime.id}/`">
            <div>
            <img :src="anime.cover_img_large" alt="Anime Image"/>
            <div>{{ anime.romaji_title }}</div>
            </div>
        </RouterLink>
        
    </div>
</template>