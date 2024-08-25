<script setup>
import { RouterLink } from 'vue-router';
import { defineProps,reactive} from 'vue';

const props = defineProps({
    staff:Object
})

</script>

<template>
    <div>
        <RouterLink :to="`/staffs/${props.staff.id}/`">
            <img :src="props.staff.img_med || props.staff.img_large" alt="staff img">
            <p>{{ props.staff.name || props.staff.name_native || "Staff name" }}</p>
        </RouterLink>
    </div>

</template>