<script setup>
import { ref, defineProps, onMounted, reactive, computed} from 'vue';
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
                // "Authorization" : `token ${stateAuth.userAuth.token}`
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
                    // "Authorization" : `token ${stateAuth.userAuth.token}`
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

const editContent = reactive({
    content: currentComment.data.content
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
    editContent.content = currentComment.data.content
    isEditing.value = !isEditing.value
}

const isReplying = ref(false)
const toggleReply  = () => {
    isReplying.value = ! isReplying.value
}
const editComment = async () => {
    if (editContent.content.length > 0){
        currentComment.data.content = editContent.content
        try{
        const response = await axios.put(comment.info.url, currentComment.data ,{
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

const getRepliedContent = computed(() => {
    let description = repliedComment.data.content
    description = description.substring(0, 20) + '...';
    return description;
})
</script>

<template>
    <div class="px-2 py-1 border-2 border-gray-500 border-dashed mx-auto my-2 max-w-sm">
        <div id="thread-area">
        <div id="header">
            <div id="userinfo" class="w-full font-medium text-gray-500 flex-row justify-between flex items-center">
                {{ comment.info.user.username || "Username" }} 
                <div v-if=" stateAuth.isAuthenticated && stateAuth.userAuth.user.username === comment.info.user.username"> 
                    <span  @click="toggleEdit" class="hover:text-blue-600 hover:cursor-pointer mr-2 px-1">Edit</span> 
                    <span  @click="deleteComment" class="hover:text-red-600 hover:cursor-pointer px-1">Delete</span> 
                </div>
                </div>
            <div id="title-time" class="w-full font-medium text-gray-500 flex-row justify-between flex items-center text-sm" >
                <div id="time">{{ comment.info.created_at || "Time created" }}</div>
            </div>
            <div v-if="comment.info.reply_to" class="text-sm mt-1 mb-1 ">
                <div> Reply to: </div>
                
                <div> {{ getRepliedContent }} </div>
            </div>
        </div>
        <div id="body-edit" class="p-1 rounded-md border border-gray-500 px-1">
            <div v-if="!isEditing" id="body">
                {{ comment.info.content }}
            </div>
            <div v-if="isEditing" id="edit">
                <textarea class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none
                 focus:ring-0 focus:border-gray-600" rows="5" cols="40" name="edit" id="edit" v-model="editContent.content"></textarea>
                <button class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" @click="editComment">Confirm</button>
                <button  class="px-5 py-1 mt-2 mb-2 bg-red-300 text-red-600 border-2 border-red-950
                font-bold rounded-xl  w-full min-w-fit hover:bg-red-800 hover:text-white" @click="toggleEdit">Cancel</button>
            </div>
        </div>
        
        <div v-if="stateAuth.isAuthenticated" id="footer" class="mt-1">
           <div v-if="!isReplying" @click="toggleReply" class="hover:text-blue-600 hover:cursor-pointer mr-2 px-1">reply</div>
           <div v-if="isReplying" id="reply-box">
            <div id="reply-form">
                <form>
                    <textarea class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none
                    focus:ring-0 focus:border-gray-600" rows="5" cols="40" name="reply" id="reply" v-model="replyComment.content"></textarea>
                    <button  class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                    font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" @click.prevent="handleReply">Post</button>
                    <button class="px-5 py-1 mt-2 mb-2 bg-red-300 text-red-600 border-2 border-red-950
                    font-bold rounded-xl  w-full min-w-fit hover:bg-red-800 hover:text-white" @click.prevent="toggleReply">Cancel</button>

                </form>
            </div>
        </div>
        </div>
        </div>
        
    </div>
    
</template>