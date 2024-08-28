<script setup>
import { defineProps } from 'vue';
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';
import { userState } from '@/store/userStore';
import axios from 'axios';
const user = reactive({
    username : "Username....",
    password : "abc",
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

    <form>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="user.username"/>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="user.password"/>
        <input @click.prevent = "submitLogin" type="submit">
    </form>
    <p>{{user.error}}</p>
</template>