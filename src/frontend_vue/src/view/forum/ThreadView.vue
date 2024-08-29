<script setup>
import { computed, onMounted, reactive, watch} from 'vue';
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
</script>

<template>

    <div id="thread-area">
        <div id="header">
        <div id="userinfo">{{ thread.content.owner.username || "Username" }}</div>
        <div id="title-time">
            <div id="title">{{ thread.content.title || "Thread title" }}</div>
            <div id="time">{{ thread.content.created_at || "Time created" }}</div>
        </div>
        </div>
        <div id="body-edit">
            <div id="body">
                {{ thread.content.body }}
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