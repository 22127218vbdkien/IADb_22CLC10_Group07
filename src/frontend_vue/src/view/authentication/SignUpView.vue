<script setup>
import { useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';
import { ref } from 'vue';
import axios from 'axios';
const user = reactive({
    username: '',
    password: '',
    email: '',
    error: '',
})
const _router = useRouter()


const handleRegister = async ()=>{
    try{
        const response =  await axios.post("/api/user/signup/", {
                username: user.username,
                password: user.password,
                email: user.email
            },
            {
                headers:{
                    "Content-Type":"application/json"
                }
            })
        console.log(response)
        if (response.status == 200 || response.status == 201 ){
            console.log(response)
            _router.push('/login/')
        }
        else {
           error.value = "Username or email has been used, please check your infomation!!!"
        }
    } catch(error){
        console.log(error)
    }
}

const resetError = () => {
    user.error = ""
}
</script>

<template>

    <form class="w-full mx-auto">
        <div>
        <label for="username" class="mb-4">Username</label>
        <input type="text" id="username" v-model="user.username" @input="resetError"/>
        </div>
        <div>
            <label for="email">Email</label>
            <input type="email" id="email" v-model="user.email"/>
        </div>
        <div>
            <label for="password">Password</label>
            <input type="password" id="password" v-model="user.password"/>
        </div>
        
        <button @click.prevent="handleRegister" type="submit" class="">Submit</button>
    </form>
    <p>{{ user.error }}</p>
    
</template> 