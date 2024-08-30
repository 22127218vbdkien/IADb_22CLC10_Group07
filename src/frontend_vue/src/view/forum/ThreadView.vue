<script setup>
import { computed, onMounted, reactive, ref} from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';
import { userState } from '@/store/userStore';
import { apiURL } from '@/searchService/apiSearch';
import CommentCard from '@/components/comment/CommentCard.vue';
import { comment } from 'postcss';
const stateAuth = userState()
const _router = useRouter()
const _route = useRoute()
const thread_id = _route.params.id 

const thread = reactive({
    content:{
        url: "",
        id: 0,
        title: "0",
        body: "0",
        view_count: 0,
        comment_count: 0,
        created_at: "",
        updated_at: "",
        owner: {}, 
        comments: [] 
    }
})


const editContent = reactive({
    data:"",
})
const commentThread = reactive({
    thread_id: computed(() => {return apiURL() + `/threads/${thread_id}/`}),
    reply_to: null,
    content: ""
})
onMounted(async () => {
    try{
            const response = await axios.get(`/api/threads/${thread_id}/`)
            if(response.status === 200 || response.status === 201)
                thread.content = response.data
                console.log(response)
        }catch(error){
            console.log(error)
    }
})

const handleComment = async () => {
    if (commentThread.content.length > 0){
        try{
            const response = await axios.post('/api/comments/', commentThread,  {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization" : `token ${stateAuth.userAuth.token}`
                }
            }).catch((error) => {
                return error.response
            })
            if (response.status === 200 || response.status === 201){
                alert('Create successfuly')
            }
            else{
                alert('Can not create')
            }
        }catch(error){
            console.log(error)
        }
    }   
        
}

const isEditing = ref(false)
const toggleEdit = () => {
    editContent.content = thread.content.body
    isEditing.value = !isEditing.value
}


const editThread = async () => {
    if (editContent.content.length > 0){
        thread.content.body = editContent.content
        try{
        const response = await axios.put(thread.content.url, thread.content ,{
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        }).catch((error) => {
            return error.response
        })
        console.log(response)
       
    }catch(error){
        console.log(error)
    }
    }
    
}

const deleteThread = async () => {
    const thread_url = apiURL() + `/threads/${thread_id}/`
    try{
        const response = await axios.delete(thread_url ,{
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        }).catch((error) => {
            return error.response
        })
        if (response.status === 204 || response.status === 201){
            alert('Delete successfuly')
        }
        else{
            alert('Can not delete')
        }
    }catch(error){
        console.log(error)
    }
}
</script>

<template>

    <section class=" border-gray-500 min-w-96 max-w-5xl mx-auto mt-10 flex flex-col justify-center items-center">
        <div class="mb-4">
            <h1 class="text-gray-700 font-bold text-2xl">
                Thread Content
            </h1>
        </div>
        <section id="thread-area" class="p-1 rounded-md border-2 border-gray-500 w-full max-w-xl mx-auto  mt-4">
            
            <div id="header" class="flex flex-col">
                <div id="userinfo" class="flex-row justify-between flex items-center" >
                    <div id="title" class="text-gray-800 font-semibold">{{ thread.content.title || "Thread title" }}</div>
                    <div v-if="  stateAuth.isAuthenticated && stateAuth.userAuth.user.username === thread.content.owner.username"> 
                        <span class="hover:text-blue-600 hover:cursor-pointer mr-2 px-1" @click="toggleEdit">Edit</span> 
                        <span class="hover:text-red-600 hover:cursor-pointer px-1"   @click="deleteThread">Delete</span> 
                    </div>
                </div>
                <div id="title-time" class="w-full font-medium text-gray-500 flex-row justify-between flex items-center">
                    <div> {{ thread.content.owner.username || "Username" }} </div>
                    <div id="time">{{ thread.content.created_at || "Time created" }}</div>
                </div>
            </div>
            <div id="body-edit" class="p-1 rounded-md border border-gray-500 px-1">
                <div v-if="!isEditing" id="body">
                    {{ thread.content.body }}
                </div>
                <div v-if="isEditing">
                    <textarea class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" rows="5" cols="40"  name="edit" id="edit" v-model="editContent.content"></textarea>
                    <button class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                    font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" @click="editThread">Confirm</button>
                    <button class="px-5 py-1 mt-2 mb-2 bg-red-300 text-red-600 border-2 border-red-950
                    font-bold rounded-xl  w-full min-w-fit hover:bg-red-800 hover:text-white" @click="toggleEdit">Cancel</button>
                </div>
            </div>
            
            <div id="footer" class="w-full font-medium text-gray-500 flex-row flex items-center">
                <div id="views" class="px-1 py-1">
                    <i class="pi pi-eye"></i>
                    {{ thread.content.view_count || "Views" }}
                </div>
                <div id="views" class="px-1 py-1">
                    <i class="pi pi-comment"></i>
                    {{ thread.content.comment_count || "Comment" }}
                </div>
            </div>
        </section>

        <div v-if="stateAuth.isAuthenticated" id="reply-box" class="mt-10 mw">
            <h2 class="font-semibold block mb-1 text-sm  text-gray-900" >Post a Reply</h2>
            <div id="reply-form">
                <form>
                    <textarea class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" rows="5" cols="40" name="reply" id="reply" v-model="commentThread.content"></textarea>
                    <button class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                    font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" type=submit @click.prevent="handleComment">Post</button>
                </form>
            </div>
        </div>
        <div class="mb-4 mt-4">
                <h1 class="text-gray-700 font-bold text-2xl">
                    Comment
                </h1>
        </div>
        <section class="mt-4 w-full max-w-xl">
            
            <div id="comment-area">
                <div id="comment-frame" v-if="thread.content.comments.length > 0">
                    <CommentCard v-for="item in thread.content.comments" :key="item.id" :thread-url="thread.content.url" :info="item"></CommentCard>
                </div>
            </div>
        </section>
    </section>
    
    

    


</template>