<template>
    <div class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 
    left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)]
    max-h-full bg-black bg-opacity-60 flex">
        <div class="p-4 w-full max-w-md max-h-full bg-blue-50 mx-auto my-auto top-auto py-4 px-8 rounded">
            <div>
                <h3>Add anime to collection</h3>
                <i class="pi pi-times" @click="()=>emit('modal-close')"></i>
            </div>
            <div v-if="!isCollected">
                <form>
                    <div>
                        <label for="is_favorite">Is Favorite</label>
                        <input id="is_favorite" type="checkbox" v-model="formInfo.content.is_favorite">
                    </div>
                    <div>
                        <TagFilter filter-name="list" :options="listName.choices" @change-tag-lists="updateList"></TagFilter>
                    </div>
                    <div>
                        <label for="score">Score</label>
                        <input id="score" type="number" min="0" max="100" v-model="formInfo.content.score">
                    </div>
                    <div>
                        <label for="progress">Progress</label>
                        <input id="progress" type="number" min="0"  v-model="formInfo.content.progress">
                    </div>
                    <div>
                        <label for="finish_date">Finish Date</label>
                        <input id="finish_date" type="datetime-local" v-model="formInfo.content.finish_date">
                    </div>
                    <div> 
                        <label for="notes">Notes</label>
                        <textarea id="notes" rows="4" cols="50"  v-model="formInfo.content.notes"></textarea>

                    </div>
                    <button type="submit" @click.prevent="handleAddAnimeToCollection">Submit</button>
                </form>
            </div>
            <div v-if="isCollected">
                <form>
                    <div>
                        <label for="is_favorite">Is Favorite</label>
                        <input id="is_favorite" type="checkbox" v-model="animeInCollection.content.is_favorite">
                    </div>
                    <div>
                        <TagFilter filter-name="list" :options="listName.choices" :has-value="animeInCollection.content.in_list" @change-tag-lists="updateCollectedList"></TagFilter>
                    </div>
                    <div>
                        <label for="score">Score</label>
                        <input id="score" type="number" min="0" max="100" v-model="animeInCollection.content.score">
                    </div>
                    <div>
                        <label for="progress">Progress</label>
                        <input id="progress" type="number" min="0"  v-model="animeInCollection.content.progress">
                    </div>
                    <div>
                        <label for="finish_date">Finish Date</label>
                        <input id="finish_date" type="datetime-local" v-model="animeInCollection.content.finish_date">
                    </div>
                    <div> 
                        <label for="notes">Notes</label>
                        <textarea id="notes" rows="4" cols="50"  v-model="animeInCollection.content.notes"></textarea>

                    </div>
                    <button type="submit" @click.prevent="handleUpdateAnimeInCollection">Update</button>
                    <button type="submit" class="text-red-600" @click.prevent="deleteAnimeInCollection">Delete</button>
                </form>
            </div>
            
        </div>
        

    </div>

</template>

<script setup>
import { userState } from '@/store/userStore';
import axios from 'axios';
import {ref, reactive, defineProps, computed, defineEmits, capitalize} from 'vue';
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
    content:{   
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
    }
    
})

const animeInCollection = reactive({
    content:{
        url: null,
        user_id: null,
        is_favorite: null,
        in_list: null,
        score: null,
        progress: null,
        start_date: null,
        finish_date: null,
        notes: null,
        anime_id: null
    }
})

// Check in this anime is in collection (favorite included)

const isCollected = ref(false)
const incollection_url = ref("")
onMounted(async () => {
    try{
        const response = await axios.get('/api/animeincollection/', {
            params: {
                search: props.anime_id
            },
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        }).catch((error)=>{
            return error.response
        })
        console.log(response)
        if (response.status === 200){
            if (response.data['count'] > 0){
                isCollected.value = true
                incollection_url.value = response.data['results'][0].url
                console.log(incollection_url.value)
                try{
                    const collection_response =  await axios.get(incollection_url.value, {
                        headers:{
                            "Content-Type":"application/json",
                            "Authorization" : `token ${stateAuth.userAuth.token}`
                        }
                    }).catch((error)=>{
                        return error.response
                    })
                    console.log(collection_response)
                    if (collection_response.status === 200){
                        animeInCollection.content = collection_response.data
                        console.log(animeInCollection.content)
                    }
                }catch(error){
                    console.log(error)
                }
            }
        }
    }catch(error){
        console.log(error)
    }
})
const preprocess = () =>{
    if (String(formInfo.content.in_list).length === 0 || !formInfo.content.in_list)
        formInfo.content.in_list = null
    if (String(formInfo.content.score).length === 0)
        formInfo.content.score = null
    if (String(formInfo.content.progress).length === 0)
        formInfo.content.progress = null
    if (String(formInfo.content.finish_date).length === 0)
        formInfo.content.finish_date = null
    if (String(formInfo.content.notes).length === 0)
        formInfo.content.notes = null
}

const preprocessInCollection = () =>{
    if (String(animeInCollection.content.in_list).length === 0 || !animeInCollection.content.in_list)
        animeInCollection.content.in_list = null
    if (String(animeInCollection.content.score).length === 0)
        animeInCollection.content.score = null
    if (String(animeInCollection.content.progress).length === 0)
        animeInCollection.content.progress = null
    if (String(animeInCollection.content.finish_date).length === 0)
        animeInCollection.content.finish_date = null
    if (String(animeInCollection.content.notes).length === 0)
        animeInCollection.content.notes = null
}

const handleAddAnimeToCollection = async () => {
    preprocess()
    console.log((formInfo.content))
    if (!stateAuth.isAuthenticated )
        alert('User is not logged in or missing credentials. Please log in!')    
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.post('/api/animeincollection/', 
                formInfo.content, {
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
    formInfo.content.in_list = event[0]    
}

const handleUpdateAnimeInCollection = async () =>{
    preprocessInCollection()
    try{
        const response = await axios.put(incollection_url.value, 
            animeInCollection.content, {
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

const updateCollectedList = (event) =>{
    animeInCollection.content.in_list = event[0]    
}
const deleteAnimeInCollection = async () => {
    try{
        const response = await axios.delete(animeInCollection.content.url, {
            headers:{
                "Content-Type":"application/json",
                "Authorization": `token ` + stateAuth.userAuth.token
            }
            })
        if (response.status === 200 || response.status === 202 || response.status === 204 )
            alert('Remove from collection!!!')
    }catch(error){
        console.log(error)
    }
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