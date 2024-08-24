<script setup>
    import axios from 'axios';
    import AnimeCard from './AnimeCard.vue';
    import PaginationBar from '../PaginationBar.vue';
    import { reactive, defineProps , onMounted, computed} from 'vue';
    import router from '@/router';
    import { useRoute, useRouter } from 'vue-router';
    const state = reactive({
        page: {
            count: 0,
            next: "",
            previous: null,
            results:[]
        },
        indexPage: 1, 
        limit: 5
    })
    const props = defineProps({
        fecthpage: Number,
    })  

    const _router = useRouter()
    const getNextPage = async (nextpage) => {
        state.indexPage = nextpage
        try{
            const response = await axios.get(`/api/animes/`, {
                params:{
                    page: (nextpage >= 1 ? nextpage : 1)
                }
            })    
            state.page = response.data

        }catch(error){
            console.log(error)
        }
    }
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
        <PaginationBar v-bind:_start="state.indexPage" v-bind:_limit="state.limit" @change-page="getNextPage" :key="state.indexPage"></PaginationBar>
    </section>
</template>