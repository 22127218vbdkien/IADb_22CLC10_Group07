<script setup>
import { onMounted, reactive, watch } from 'vue';
import PaginationBar from '@/components/PaginationBar.vue';
import SearchBar from '@/components/search_filter/SearchBar.vue';
import parseParams from '@/searchService/apiSearch';
import { userState } from '@/store/userStore';
import { useRouter } from 'vue-router';
import axios from 'axios';
const stateAuth = userState
const _router = useRouter()
const threads =  reactive({
    results:[]
})

const query = reactive({
    content: {
        page: 1,
        search: "",
    }
    
})

onMounted(async ()=>{
    query.content = _router.query
    try{
        const response = await axios.get('/api/threads/', 
            {
                params: query.content,
                paramsSerializer: () => parseParams(params)
            }
        )
        console.log(response)
    }catch(error){
        console.log(error)
    }
})

</script>

<template>
    Forum View
</template>