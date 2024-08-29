<script setup>
import { userState } from '@/store/userStore';
import { reactive, defineEmits} from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';


const stateAuth = userState()
const emit = defineEmits(['modal-close'])
const formInfo = reactive({
    title: "",
    body:"",
    
})


const validate = () => {
    if (formInfo.title.length <= 0 || formInfo.body.length <= 0){
        alert('Please complete the form')
        return false
    }
    return true
}

const handlePostThread = async () => {
    const status = validate()
    if (status){
        try{
            const response = await axios.post('/api/threads/', formInfo, {
                headers:{
                    "Content-Type":"application/json",
                    "Authorization" : `token ${stateAuth.userAuth.token}`
                }
            })
            if (response.status === 200 || response.status === 201){
                alert('Create successfuly')
            }
        }catch(error){
            console.log(error)
        }
    }
}


</script>

<template>
    <div class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 
    left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)]
    max-h-full bg-black bg-opacity-60 flex">
        <div class="p-4 w-full max-w-md max-h-full bg-blue-50 mx-auto my-auto top-auto py-4 px-8 rounded">
            <div>
                <h3>Post thread</h3>
                <i class="pi pi-times" @click="()=>emit('modal-close')"></i>
            </div>
            <div>
                <form>
                <div>
                    <label for="title">Title</label>
                    <input id="title" type="text" v-model="formInfo.title">
                </div>
                <div>
                    <label for="title">Body</label>
                    <textarea id="body" type="text" v-model="formInfo.body"></textarea>
                </div>
                
                <button type="submit" @click.prevent="handlePostThread">Submit</button>
            </form>
            </div>
            
        </div>
        

    </div>
</template>