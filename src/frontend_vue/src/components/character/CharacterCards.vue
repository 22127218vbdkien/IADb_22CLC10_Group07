<script setup>
    import axios from 'axios';
    import PaginationBar from '../PaginationBar.vue';
    import { reactive, defineProps , onMounted} from 'vue';
    import CharacterCard from './CharacterCard.vue';
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

    const getNextPage = async (nextpage) => {
        state.indexPage = nextpage
        try{
            const response = await axios.get(`/api/characters/`, {
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
            const response = await axios.get(`/api/characters/`, {
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
        <!-- <div>{{ state.page.results }}</div> -->
        <CharacterCard v-for="character in state.page.results" :key="character.id" :character="character"></CharacterCard>
        <PaginationBar v-bind:_start="state.indexPage" v-bind:_limit="state.limit" @change-page="getNextPage" :key="state.indexPage"></PaginationBar>
    </section>
</template>