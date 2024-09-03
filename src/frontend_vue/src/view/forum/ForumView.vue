<script setup>
import {ref, onMounted, reactive, watch } from 'vue';
import PaginationBar from '@/components/PaginationBar.vue';
import SearchBar from '@/components/search_filter/SearchBar.vue';
import parseParams from '@/searchService/apiSearch';
import { userState } from '@/store/userStore';
import { useRouter } from 'vue-router';
import ThreadCard from '@/components/thread/ThreadCard.vue';
import ThreadPostBox from '@/components/thread/ThreadPostBox.vue';
import axios from 'axios';
const stateAuth = userState()
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

const showPostThread = ref(false)
const togglePostThread = () => {
    showPostThread.value = !showPostThread.value
}
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
    }catch(error){
        console.log(error)
    }
})

</script>

<template>  

    <section v-if="stateAuth.isAuthenticated" class="max-w-6xl mx-auto mt-10 mb-4 px-4 py-2 flex flex-col justify-center items-center">
        <h1 class="text-gray-700 font-bold text-xl">
                Post a thread now ヾ(≧▽≦*)o
        </h1>
        <div id="add-thread">
            <button @click="togglePostThread" class="py-2 px-4 my-2 border-2 border-blue-500 bg-blue-100 rounded-xl hover:bg-blue-300 text-sm ">Add a thread</button>
        </div>

    </section>
    

    
    <section id="thread-section" class="max-w-6xl mx-auto mt-10 mb-4 px-4 py-2 ">
        <h1 class="text-gray-700 font-bold text-2xl flex items-center justify-between flex-col w-full">
            Thread section
        </h1>
        <div id="thread-frame" v-if="threads.results.length > 0" class="max-w-full flex items-center justify-between flex-col">
            <ThreadCard v-for="item in threads.results" :key="item.id" :thread="item" class="py-2"></ThreadCard>
        </div>
        <div v-else class="text-gray-700 font-semibold text-xl flex items-center justify-between flex-col w-full"> There is no thread to display</div>
    </section>
    <ThreadPostBox v-if="showPostThread" @modal-close="togglePostThread"></ThreadPostBox>
</template>