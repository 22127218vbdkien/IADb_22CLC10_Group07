<script setup>
import { useRoute, useRouter } from 'vue-router';
import { reactive } from 'vue';

const user = reactive({
    password: "",
    username: "",
    email: "",
})
</script>

<template>

    <form class="max-w-sm mx-auto"></form>
    <div>
        <label for="username" class="mb-4">Username</label>
        <input type="text" id="username"/>
    </div>
    <div>
        <label for="password">Password</label>
        <input type="password" id="password"/>
    </div>
    <button type="submit" class=""></button>
</template> 