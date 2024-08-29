<script setup>
import PaginationBar from '@/components/PaginationBar.vue';
import { useRoute, useRouter} from 'vue-router';
import SearchBar from '@/components/search_filter/SearchBar.vue';
import TagFilter from '@/components/search_filter/TagFilter.vue';
import { reactive, watch , ref,onMounted, capitalize} from 'vue';
import parseParams from '@/searchService/apiSearch';
import axios from 'axios';
import StaffCard from '@/components/staff/StaffCard.vue';
const _router = useRouter()
const _route = useRoute()

const state = reactive({
    page: {
        count: 0,
        next: "",
        previous: null,
        results:[]
    }
})

const userQuery = reactive({
    content: {
        search: "",
        ordering: "",
        page: 1
    }, 
    limit:5
})

const orderingTags = ref([
    {
        query: "name",
        name: "Name - ascending"
    },
    {
        query: "-name",
        name: "Name - descending"
    },
    {
        query: "favorites",
        name: "Favorites - ascending"
    },
    {
        query: "-favorites",
        name: "Favorites - descending"
    }

])

onMounted( async () => {
        const query = _route.query
        userQuery.query = query
        try{
            const response = await axios.get('/api/staffs/', {
                params: query,
                paramsSerializer: (params) => parseParams(params)
            }).catch((error) => {return error.response})
            if (response.status === 200){
                state.page = response.data
                console.log(state.page)
            }
        }catch(error){
            console.log(error)
        }
})

const changePage = (event) =>{
    userQuery.content.page = event
    _router.push({ path: _route.fullPath, query:userQuery.content })
}
const changeSearch = (event) => {
    userQuery.content.search = event
}

const changeTag = (event) =>{
    userQuery.content.ordering = event
}
const handleQuery = () => {
    userQuery.content.page = 1
    _router.push({ path: _route.fullPath, query:userQuery.content })
}
watch( () => _route.query,
    async (query) => {
        userQuery.query = query
        try{
            const response = await axios.get('/api/staffs/', {
                params: query,
                paramsSerializer: (params) => parseParams(params)
            }).catch((error) => {return error.response})
            if (response.status === 200){
                state.page = response.data
                console.log(state.page)
            }
        }catch(error){
            console.log(error)
        }
})
    

</script>

<template>

    <div class="max-w-6xl mx-auto mt-10 mb-4 px-4 py-2">
        <div class="flex flex-row items-center justify-between w-full">
            <div class="w-full pr-2 ">
                <SearchBar @sendChange="changeSearch" target="Staff"></SearchBar>
            </div>
            <div class="w-max">
                <TagFilter @changeTagLists="changeTag" :options="orderingTags" filterName="Ordering"></TagFilter>
            </div>
        </div>
        <div class="w-full flex-row-reverse flex">
            <button @click="handleQuery" class="py-2 px-4 my-2 border-2 border-blue-500 bg-blue-100 rounded-xl hover:bg-blue-300 text-sm ">Click to search</button>
        </div>
    </div>

    <section class="max-w-6xl mx-auto mt-10 mb-4 px-4 py-2">
        <div class="mb-4">
            <h1 class="text-gray-700 font-bold text-2xl">
                Staff Section
            </h1>
        </div>
        <div class="max-w-full flex items-center justify-between flex-col">
            <div id="character-frame" class="grid grid-cols-5 max-w-5xl gap-x-10 gap-y-4 grid-flow-row">
                <StaffCard v-for="staff in state.page.results" :key="staff.id" :staff="staff"></StaffCard>
            </div>
            <PaginationBar v-bind:_start="userQuery.content.page" v-bind:_limit="userQuery.limit" :key="userQuery.content.page" v-on:changePage="changePage"></PaginationBar>
        </div>
    </section>

</template>