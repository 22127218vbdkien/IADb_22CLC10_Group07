<script setup>
import { defineProps } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';
import { userState } from '@/store/userStore';
import axios from 'axios';
const user = reactive({
    username : "",
    password : "",
    error: ""
})
const _router = useRouter()
const stateAuth = userState()

const submitLogin = async () =>{
    await stateAuth.login(user.username, user.password, _router)
    if (! stateAuth.isAuthenticated){
        user.error = 'Login failed. Please check your credentials.'
    }
}

const resetError = () =>{
    user.error = ""
}
</script>

<template>
    <div>
        <form>
            <label for="username" >Username</label>
            <input type="text" id="username" placeholder="..." v-model="user.username" @input="resetError"/>
            <label for="password">Password</label>
            <input type="password" id="password" placeholder="..." v-model="user.password" @input="resetError"/>
            <input @click.prevent = "submitLogin" type="submit">
        </form>
        <p>{{user.error}}</p>
    </div>
    <RouterLink to="/signup/">Create a new account <i class="pi pi-arrow-right"></i></RouterLink>
</template>