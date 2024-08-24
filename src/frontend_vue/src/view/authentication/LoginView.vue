<script setup>
import { defineProps } from 'vue';
import { RouterLink } from 'vue-router';
import { reactive } from 'vue';

const user = reactive({
    username : "Username....",
    password : "abc"
})


const submitLogin = () =>{
    try{
        const response =  fetch("/api/login/", {
            method: "POST",
            body: JSON.stringify(user)
        }).then(response => {
            if (response.ok)
                console.log(response)
        }).then(data => {
            return data
        })
        console.log(response)
    } catch (error){
        console.log(error)
    }
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
</template>