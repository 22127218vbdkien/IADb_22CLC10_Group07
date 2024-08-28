<template>
    <div class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 
    left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)]
    max-h-full bg-black bg-opacity-60 flex">
        <div class="p-4 w-full max-w-md max-h-full bg-blue-50 mx-auto my-auto top-auto py-4 px-8 rounded">
            <div>
                <h3>Add anime to collection</h3>
                <i class="pi pi-times" @click="()=>emit('modal-close')"></i>
            </div>
            <div>
                <form>
                <div>
                    <label for="is_favorite">Is Favorite</label>
                    <input id="is_favorite" type="checkbox" v-model="formInfo.is_favorite">
                </div>
                <div>
                    <TagFilter filter-name="list" :options="listName.choices"></TagFilter>
                </div>
                <div>
                    <label for="score">Score</label>
                    <input id="score" type="number" min="0" max="100" v-model="formInfo.score">
                </div>
                <div>
                    <label for="progress">Progress</label>
                    <input id="progress" type="number" min="0"  v-model="formInfo.progress">
                </div>
                <div>
                    <label for="notes">Notes</label>
                    <textarea id="notes" rows="4" cols="50"  v-model="formInfo.notes"></textarea>

                </div>
                <button type="submit" @click.prevent="handleAddAnimeToCollection">Submit</button>
            </form>
            </div>
            
        </div>
        

    </div>

</template>

<script setup>
import { userState } from '@/store/userStore';
import axios from 'axios';
import {ref, reactive, defineProps, computed, defineEmits} from 'vue';
import { onMounted } from 'vue';
import TagFilter from '../search_filter/TagFilter.vue';
import { apiURL } from '@/searchService/apiSearch';
const stateAuth = userState()
const listName = reactive({
    choices: [
        {
            query: "WATCHING",
            name: "Watching"
        },
        {
            query: "COMPLETED",
            name: "Completed"
        },
        {
            query: "PAUSED",
            name: "Paused"
        },
        {
            query: "DROPPED",
            name: "Dropped"
        },
        {
            query: "PLANNING",
            name: "Planning"
        }
    ]
})
const props = defineProps({
    anime_id: Number,
    anime_id_url: String
})

const emit = defineEmits(['modal-close'])

const formInfo = reactive({
    is_favorite: false,
    in_list: null,
    score: null,
    progress: null,
    finish_date: null,
    notes: "",
    anime_id: computed(() =>{ 
        if (props.anime_id_url)
            return  props.anime_id_url
        return apiURL() + `/animes/${props.anime_id}/`
    })
})

const handleAddAnimeToCollection = async () => {
    console.log(JSON.stringify(formInfo))
    if (!stateAuth.isAuthenticated )
        alert('User is not logged in or missing credentials. Please log in!')    
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.post('/api/animeincollection/', 
                formInfo, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            console.log(response)
        }catch(error){
            console.log(error)
        }
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
    }
}

const updateList = (event) =>{
    formInfo.in_list = event
}
</script>

<style scoped>
.overlay-container {
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
background: rgba(0, 0, 0, 0.6);
justify-content: center;
align-items: center;
z-index: 0;
}


</style>