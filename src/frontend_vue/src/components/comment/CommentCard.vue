<script setup>
import { defineProps, onMounted, reactive} from 'vue';
import { userState } from '@/store/userStore';
import axios from 'axios';
const stateAuth = userState()
const comment = defineProps({
    info: Object,
    threadUrl: String,
})

const replyComment = reactive({
    thread_id: comment.threadUrl,
    reply_to: comment.info.url,
    content: ""
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
</script>

<template>
    <div>
        <div id="thread-area">
        <div id="header">
            <div id="userinfo">{{ comment.info.user.username || "Username" }} </div>
            <div id="title-time">
                <div id="time">{{ comment.info.created_at || "Time created" }}</div>
            </div>
            <div v-if="comment.info.reply_to">{{ repliedComment.data }}</div>
        </div>
        <div id="body">
            {{ comment.info.content }}
        </div>
        <div id="footer">
           <div>reply</div>
        </div>
        </div>
        <div id="reply-box">
            <div id="reply-form">
                <form>
                    <textarea name="reply" id="reply" v-model="replyComment.content"></textarea>
                    <button @click="handleComment"></button>
                </form>
            </div>
        </div>
    </div>
    
</template>