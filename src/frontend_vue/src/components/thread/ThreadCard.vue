<script setup>
import { defineProps } from 'vue';
import { computed } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
    thread: Object
})


const displayBody = computed(() => {
    let description = props.thread.body;
    if (description.length > 150)
        description = description.substring(0, 150) + '...';
    return description;
})
</script>

<template>

    <div class="hover:border-blue-600 hover:border-dashed hover:border-4 px-2">
        <RouterLink :to="`/thread/${thread.id}/`">
            <div class="p-1 rounded-md border-2 border-gray-500 min-w-96 max-w-md">
                <div id="header flex flex-col">
                    <div id="title" class="text-gray-800 font-semibold">{{ thread.title || "Thread title" }}</div>
                    <div id="title-time" class="w-full font-medium text-gray-500 flex-row justify-between flex items-center">
                        <div id="userinfo" class="font-bold  ">{{ thread.owner.username || "Username" }}</div>
                        <div id="time" class="text-sm">{{ thread.created_at || "Time created" }}</div>
                    </div>
                    
                </div>
                <div id="body" class="p-1 rounded-md border border-gray-500 px-1">
                        {{displayBody}}
                    </div>
                    <div id="footer" class="w-full font-medium text-gray-500 flex-row flex items-center">
                        <div id="views" class="px-1 py-1">
                            <i class="pi pi-eye"></i>
                            {{ thread.view_count || "Views" }}
                        </div>
                    
                        <div id="views" class="px-1 py-1">
                            <i class="pi pi-comment"></i>
                            {{ thread.comment_count || "Comment" }}
                        </div>
                    </div>
            </div>
            
        </RouterLink>
        
    </div>

</template>