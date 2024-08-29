<script setup>
import { onMounted, reactive, watch } from 'vue';
import PaginationBar from '@/components/PaginationBar.vue';
import SearchBar from '@/components/search_filter/SearchBar.vue';
import parseParams from '@/searchService/apiSearch';
import { userState } from '@/store/userStore';
import { useRouter } from 'vue-router';
import ThreadCard from '@/components/thread/ThreadCard.vue';
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
        threads.results = response.data['results']
        console.log(response)
    }catch(error){
        console.log(error)
    }
})

</script>

<template>

    <div id="add-thread">
        <button>Add a thread</button>
    </div>

    <div id="thread-section">
        <h2>Thread section</h2>
        <div id="thread-frame" v-if="threads.results.length > 0">
            <ThreadCard v-for="item in threads.results" :key="item.id" :thread="item"></ThreadCard>
        </div>
        <div v-else> There is no thread to display</div>
    </div>
   
</template>