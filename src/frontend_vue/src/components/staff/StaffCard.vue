<script setup>
import { RouterLink } from 'vue-router';
import { defineProps,reactive} from 'vue';

const props = defineProps({
    staff:Object
})

</script>

<template>
    <div class="card-container hover:border-blue-600 hover:border-4 hover:border-dashed w-40 px-1 py-2 min-w-24 min-h-32">
        <RouterLink :to="`/staffs/${props.staff.id}/`">
            <div class="flex flex-col items-center">
                <img :src="props.staff.img_med || props.staff.img_large" alt="staff img">
                <p class="text-sm mt-1">{{ props.staff.name || props.staff.name_native || "Staff name" }}</p>
            </div>
            
        </RouterLink>
    </div>

</template>