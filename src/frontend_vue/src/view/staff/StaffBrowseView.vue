<script setup>
import StaffCards from '@/components/staff/StaffCards.vue';
import PaginationBar from '@/components/PaginationBar.vue';
import { useRoute, useRouter , onBeforeRouteUpdate} from 'vue-router';
import { reactive, watch } from 'vue';
const _router = useRouter()
const _route = useRoute()

const state = reactive({
    indexPage: 1, 
    limit: 5
})
state.indexPage = (_route.query.page ? Number(_route.query.page) :state.indexPage)
console.log(state.indexPage)
watch(() => _route.query.page ? Number(_route.query.page) :state.indexPage,
    (newPage) => {
    if (state.indexPage != Number(newPage) && newPage)
        state.indexPage = Number(newPage)
})
    
</script>

<template>
    <StaffCards :fecthpage="state.indexPage" :key="state.indexPage"></StaffCards>
    <PaginationBar v-bind:_start="state.indexPage" v-bind:_limit="state.limit" :key="state.indexPage"></PaginationBar>

</template>