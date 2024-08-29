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
        <div class="flex flex-col items-center bg-white w-full max-w-sm py-4 rounded-3xl shadow-lg">
            <div class="flex flex-row items-center">
                <h3 class="text-xl text-center font-bold leading-tight tracking-tight text-gray-900 md:text-2xl mr-4">Post thread</h3>
                <i class="pi pi-times" @click="()=>emit('modal-close')"></i>
            </div>
            <div>
                <form>
                <div>
                    <label class="font-semibold block mb-1 text-sm  text-gray-900" for="title">Title</label>
                    <input class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" id="title" type="text" v-model="formInfo.title">
                </div>
                <div>
                    <label class="font-semibold block mb-1 text-sm  text-gray-900" for="body">Body</label>
                    <textarea class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" id="body" type="text" rows="5" cols="40" v-model="formInfo.body"></textarea>
                </div>
                
                <button class="px-5 py-1 mt-2 mb-2 bg-blue-300 text-gray-900 border-2 border-blue-950
                font-bold rounded-xl  w-full min-w-fit hover:bg-blue-800 hover:text-white" type="submit" @click.prevent="handlePostThread">Submit</button>
            </form>
            </div>
            
        </div>
        

    </div>
</template>