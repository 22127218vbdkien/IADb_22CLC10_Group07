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
    <div>
        <SearchBar @sendChange="changeSearch" target="Staff"></SearchBar>
        <TagFilter @changeTagLists="changeTag" :options="orderingTags" filterName="Ordering"></TagFilter>
        <button @click="handleQuery">Click to search</button>
    </div>
    <div id="staff-frame">
        <StaffCard v-for="staff in state.page.results" :key="staff.id" :staff="staff"></StaffCard>
    </div>
    <PaginationBar v-bind:_start="userQuery.content.page" v-bind:_limit="userQuery.limit" :key="userQuery.content.page" v-on:changePage="changePage"></PaginationBar>

</template>