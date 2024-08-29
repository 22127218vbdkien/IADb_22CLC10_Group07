<script setup>
import { defineProps } from 'vue';
import { computed } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
    thread: Object
})

</script>

<template>

<div>
    <RouterLink :to="`/thread/${thread.id}/`">
        <div id="header">
        <div id="userinfo">{{ thread.owner.username || "Username" }}</div>
        <div id="title-time">
            <div id="title">{{ thread.title || "Thread title" }}</div>
            <div id="time">{{ thread.created_at || "Time created" }}</div>
        </div>
        </div>
        <div id="body">

        </div>
        <div id="footer">
            <div id="views">
                <i class="pi pi-eye"></i>
                {{ thread.view_count || "Views" }}
            </div>
            <div id="views">
                <i class="pi pi-comment"></i>
                {{ thread.comment_count || "Comment" }}
            </div>
        </div>
    </RouterLink>
    
</div>

</template>