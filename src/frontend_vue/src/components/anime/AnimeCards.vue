<script setup>
    import axios from 'axios';
    import AnimeCard from './AnimeCard.vue';
    import PaginationBar from '../PaginationBar.vue';
    import { reactive, defineProps , onMounted, computed} from 'vue';
    import router from '@/router';
    
    const state = reactive({
        page: {
            count: 0,
            next: "",
            previous: null,
            results:[]
        }
    })
    const props = defineProps({
        fecthpage: Number,
    })  

    
    onMounted(async () => {
        try{
            const response = await axios.get(`/api/animes/`, {
                params:{
                    page: (props.fecthpage >= 1 ? props.fecthpage : 1)
                }
            })    
            state.page = response.data

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