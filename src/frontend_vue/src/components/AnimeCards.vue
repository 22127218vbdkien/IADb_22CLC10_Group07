<script setup>
    import AnimeCard from './AnimeCard.vue';
    import { reactive, defineProps , onMounted } from 'vue';
    const state = reactive({
        page: {}
    })

    onMounted(async () => {
        try{
            const response = await fetch('/api/animes/')    
            state.page = await response.json()

        }catch(error){
            console.log(error)
        }
    })
</script>

<template>
    <section>
        <AnimeCard v-for="anime in state.page.results" :key="anime.id" :anime="anime"/>
    </section>
</template>