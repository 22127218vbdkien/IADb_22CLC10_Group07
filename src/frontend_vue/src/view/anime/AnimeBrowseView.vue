<script setup>
    import AnimeCards from '@/components/anime/AnimeCards.vue';
    import PaginationBar from '@/components/PaginationBar.vue';
    import { useRoute, useRouter , onBeforeRouteUpdate} from 'vue-router';
    import { reactive, watch } from 'vue';
    import AnimeSearchAndFilter from '@/components/search_filter/AnimeSearchAndFilter.vue';
    const _router = useRouter()
    const _route = useRoute()

    const state = reactive({
        indexPage: 1, 
        limit: 5
    })
    const changePage = (event) =>{
        console.log(event)
        _router.push({ path: _route.fullPath, query:{page:event} })
    }

    watch(() => _route.query.page ? Number(_route.query.page) :state.indexPage,
        (newPage) => {
        if (state.indexPage != Number(newPage) && newPage)
            state.indexPage = Number(newPage)
    })
    
</script>

<template>
    <AnimeCards :fecthpage="state.indexPage" :key="state.indexPage"></AnimeCards>
    <PaginationBar v-bind:_start="state.indexPage" v-bind:_limit="state.limit" :key="state.indexPage" v-on:changePage="changePage"></PaginationBar>
</template>