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
        }
    })
    const props = defineProps({
        fecthpage: Number,
    })  
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
    </section>
</template>