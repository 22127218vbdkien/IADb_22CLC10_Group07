<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router';
import { reactive, defineProps} from 'vue';
import TagFilter from './TagFilter.vue';
const emit = defineEmits(['sendChange'])
const sendChange = (event) =>{
            emit("sendChange", event.target.value)
}

const props = defineProps({
    target:String,
})
</script>

<template>  
    <div class="flex flex-col py-2">
        <label :for="target">Search for {{target.toUpperCase()}}</label>
        <input class="border rounded-xl w-full text-base px-2 py-1 focus: shadow-blue-500 focus:outline-none focus:ring-0 focus:border-gray-600" :id="target" type="text" placeholder="Input here" @change="sendChange">
    </div>
    
</template>