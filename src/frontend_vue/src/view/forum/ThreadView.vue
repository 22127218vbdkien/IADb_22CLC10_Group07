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
const currentUserName = stateAuth.userAuth.user.username

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
    if (!stateAuth.isAuthenticated )
        alert('User is not logged in or missing credentials. Please log in!')    
    else if (stateAuth.userAuth.token){
        try{
            const response = await axios.get(`/api/threads/${thread_id}/`, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization": `token ` + stateAuth.userAuth.token
                }
                })
            if(response.status === 200 || response.status === 201)
                thread.content = response.data
                console.log(response)
        }catch(error){
            console.log(error)
        }
    }
    else{
        alert('User is not logged in or missing credentials. Please log in!')
    }
})

const handleComment = async () => {
    if (commentThread.content.length > 0){
        try{
            const response = await axios.post('/api/comments/', commentThread, {
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

    <div id="thread-area">
        <div id="header">
        <div id="userinfo">
            {{ thread.content.owner.username || "Username" }}
            <div v-if="currentUserName === thread.content.owner.username"> 
                <span @click="toggleEdit" class="textlink">Edit</span> 
                <span  @click="deleteThread" class="textlink">Delete</span> 
            </div>
        </div>
        <div id="title-time">
            <div id="title">{{ thread.content.title || "Thread title" }}</div>
            <div id="time">{{ thread.content.created_at || "Time created" }}</div>
        </div>
        </div>
        <div id="body-edit">
            <div v-if="!isEditing" id="body">
                {{ thread.content.body }}
            </div>
            <div v-if="isEditing">
                <textarea name="edit" id="edit" v-model="editContent.content"></textarea>
                <button @click="editThread">Confirm</button>
                <button @click="toggleEdit">Cancel</button>
            </div>
        </div>
        
        <div id="footer">
            <div id="views">
                <i class="pi pi-eye"></i>
                {{ thread.content.view_count || "Views" }}
            </div>
            <div id="views">
                <i class="pi pi-comment"></i>
                {{ thread.content.comment_count || "Comment" }}
            </div>
        </div>
    </div>
    <div id="reply-box">
        <h2>Post a Reply</h2>
        <div id="reply-form">
            <form>
                <textarea name="reply" id="reply" v-model="commentThread.content"></textarea>
                <button type=submit @click.prevent="handleComment">Post</button>
            </form>
        </div>
    </div>

    <div id="comment-area">
        <h2>Comment Section</h2>
        <div id="comment-frame" v-if="thread.content.comments.length > 0">
            <CommentCard v-for="item in thread.content.comments" :key="item.id" :thread-url="thread.content.url" :info="item"></CommentCard>
        </div>
    </div>


</template>