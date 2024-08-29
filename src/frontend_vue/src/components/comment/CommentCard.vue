<script setup>
import { ref, defineProps, onMounted, reactive} from 'vue';
import { userState } from '@/store/userStore';
import axios from 'axios';
const stateAuth = userState()
const currentUserName = stateAuth.userAuth.user.username

const comment = defineProps({
    info: Object,
    threadUrl: String,
})
const replyComment = reactive({
    thread_id: comment.threadUrl,
    reply_to: comment.info.url,
    content: ""
})

const currentComment = reactive({
    data:{
        id: 0,
        thread_id: "",
        user_id: "",
        reply_to: null,
        content: "",
        created_at: "",
        updated_at: "",
        url: ""
    }
    
})


const repliedComment = reactive({
    data:{
        id: 0,
        thread_id: "",
        user_id: "",
        reply_to: null,
        content: "",
        created_at: "",
        updated_at: "",
        url: ""
    }
    
})


onMounted(async () => {
    try{
        const response = await axios.get(comment.info.url, {
            headers:{
                "Content-Type":"application/json",
                "Authorization" : `token ${stateAuth.userAuth.token}`
            }
        })
        if (response.status === 200 || response.status === 201){
            currentComment.data = response.data
        }
    }catch(error){
        console.log(error)
    }

    if (comment.info.reply_to){
        try{
            const response = await axios.get(comment.info.reply_to, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization" : `token ${stateAuth.userAuth.token}`
                }
            })
            if (response.status === 200 || response.status === 201){
                repliedComment.data = response.data
            }
        }catch(error){
            console.log(error)
        }
    }
})

const handleReply = async () =>{
    if (replyComment.content.length > 0){
        try{
            const response = await axios.post('/api/comments/', replyComment, {
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
    isEditing.value = !isEditing.value
}

const editComment = () => {
    console.log(currentComment.data.content)
}

const deleteComment = async () => {
    try{
        const response = await axios.delete(comment.info.url ,{
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
    <div class="px-2 py-1 border-2 border-blue-500 mx-auto my-2 max-w-sm">
        <div id="thread-area">
        <div id="header">
            <div id="userinfo">{{ comment.info.user.username || "Username" }} 
                <div v-if="currentUserName === comment.info.user.username"> <span @click="toggleEdit" class="textlink">Edit</span> <span  @click="deleteComment" class="textlink">Delete</span> </div>
                </div>
            <div id="title-time">
                <div id="time">{{ comment.info.created_at || "Time created" }}</div>
            </div>
            <div v-if="comment.info.reply_to">Reply to: {{ repliedComment.content }}</div>
        </div>
        <div id="body-edit">
            <div v-if="!isEditing" id="body">
                {{ comment.info.content }}
            </div>
            <div v-if="isEditing" id="edit">
                <textarea name="edit" id="edit" v-model="currentComment.data.content"></textarea>
                <button @click="editComment">Confirm</button>
                <button @click="toggleEdit">Cancel</button>
            </div>
        </div>
        
        <div id="footer">
           <div>reply</div>
        </div>
        </div>
        <div id="reply-box">
            <div id="reply-form">
                <form>
                    <textarea name="reply" id="reply" v-model="replyComment.content"></textarea>
                    <button @click.prevent="handleReply">Post</button>
                </form>
            </div>
        </div>
    </div>
    
</template>