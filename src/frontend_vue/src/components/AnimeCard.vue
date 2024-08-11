<script setup>
    import { computed, defineProps, ref } from 'vue';
    import { RouterLink } from 'vue-router';

    const props = defineProps({
        anime:Object
    })
</script>

<template>
    <div>
        <div>
            <img :src="anime.cover_img_large" alt="Anime Image"/>
            <div>{{ anime.romaji_title }}</div>
        </div>
    </div>
</template>